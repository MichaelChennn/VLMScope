import os
import math
import numpy as np
from PIL import Image
from decord import VideoReader, cpu
import config

# ==============================================================================
#  INTERNAL HELPERS
# ==============================================================================

def _format_block(data_dict):
    """
    Helper to align colons vertically based on the longest key.
    Input: {"File Name": "video.mp4", "FPS": "30.00"}
    Output:
    • File Name : video.mp4
    • FPS       : 30.00
    """
    if not data_dict:
        return ""
    
    # 1. Find the maximum length of keys to determine padding
    max_key_len = max(len(k) for k in data_dict.keys())
    
    lines = []
    for k, v in data_dict.items():
        # 2. Dynamic padding: left-justify the key
        padded_key = k.ljust(max_key_len)
        lines.append(f"• {padded_key} : {v}")
        
    return "\n".join(lines)

def _resize_logic(image, min_pixels, max_pixels):
    """Resizes image based on pixel limits while maintaining aspect ratio."""
    width, height = image.size
    current_pixels = width * height
    target_pixels = current_pixels
    
    if current_pixels > max_pixels: target_pixels = max_pixels
    elif current_pixels < min_pixels: target_pixels = min_pixels
    
    if target_pixels == current_pixels: return image
        
    scale_factor = math.sqrt(target_pixels / current_pixels)
    new_w = int(width * scale_factor)
    new_h = int(height * scale_factor)
    
    if new_w % 2 != 0: new_w += 1
    if new_h % 2 != 0: new_h += 1
    
    return image.resize((new_w, new_h), Image.Resampling.BICUBIC)

def _extract_logic(video_name, target_fps):
    """Extracts frames and returns video metadata."""
    if not video_name: return None, None, "Please select a video."
    path = os.path.join(config.DATASET_DIR, video_name)
    
    if not os.path.exists(path):
        return None, None, f"Video not found: {path}"

    try:
        vr = VideoReader(path, ctx=cpu(0))
        video_fps = vr.get_avg_fps()
        if math.isnan(video_fps) or video_fps <= 0: video_fps = 30.0 
        
        duration = len(vr) / video_fps
        timestamps = np.arange(0, duration, 1/target_fps)
        indices = [int(t * video_fps) for t in timestamps if int(t * video_fps) < len(vr)]
        
        if not indices: return None, None, "No frames extracted."
        
        frames_np = vr.get_batch(indices).asnumpy()
        frames = [Image.fromarray(f) for f in frames_np]
        
        meta = {
            "orig_fps": video_fps,
            "duration": duration,
            "orig_res": frames[0].size  # (width, height)
        }
        
        return frames, meta, None
    except Exception as e:
        return None, None, f"Error: {str(e)}"

# ==============================================================================
#  GEMINI TOKEN LOGIC (Based on User Documentation)
# ==============================================================================

def _get_gemini_token_info(model_version, resolution_tier, num_frames):
    """
    Calculates token usage based on Model Family and Resolution.
    Data source: User provided documentation.
    """
    # Defense
    if not model_version: model_version = "Gemini 3 Pro"
    
    # Defaults
    tokens_per_frame = 0
    guidance = ""
    
    if "Gemini 3" in model_version:
        # Gemini 3 Logic
        if resolution_tier == "High":
            tokens_per_frame = 280
            guidance = "Recommended for text-heavy videos (OCR) or small details."
        else:
            # Low and Medium are treated identically in Gemini 3 (70 tokens)
            tokens_per_frame = 70
            guidance = "Optimized for context. Low/Medium are treated identically (70 tokens)."
            
    elif "Gemini 2.5" in model_version:
        # Gemini 2.5 Logic
        if resolution_tier == "Low":
            tokens_per_frame = 64
            guidance = "Lowest cost/latency."
        elif resolution_tier == "Medium":
            tokens_per_frame = 256
            guidance = "Standard usage."
        elif resolution_tier == "High":
            tokens_per_frame = 256
            guidance = "Same token count as Medium for Video in 2.5."
        else:
            # Default/Unspecified
            tokens_per_frame = 256

    total_tokens = tokens_per_frame * num_frames
    return tokens_per_frame, total_tokens, guidance

# ==============================================================================
#  PUBLIC FUNCTIONS (Called by App)
# ==============================================================================

def run_qwen_viz(video_name, fps, min_w, min_h, max_w, max_h):
    frames, meta, error = _extract_logic(video_name, fps)
    if error: return None, error, "", ""
    
    min_p = int(min_w * min_h)
    max_p = int(max_w * max_h)
    
    resized = [_resize_logic(f, min_p, max_p) for f in frames]
    
    final_w, final_h = resized[0].size
    final_pixels = final_w * final_h
    orig_w, orig_h = meta['orig_res']
    orig_pixels = orig_w * orig_h
    
    # --- Block 1: Source Info (Dict) ---
    src_data = {
        "File Name": video_name,
        "Original FPS": f"{meta['orig_fps']:.2f}",
        "Original Size": f"{orig_w} x {orig_h}",
        "Total Pixels": f"{orig_pixels:,} px",
        "Duration": f"{meta['duration']:.2f} sec"
    }
    log_source = _format_block(src_data)

    # --- Block 2: Config Info (Dict) ---
    cfg_data = {
        "Strategy": "Qwen-VL (Smart Resize)",
        "Target FPS": str(fps),
        "Min Pixels": f"{min_p:,} ({int(min_w)}x{int(min_h)})",
        "Max Pixels": f"{max_p:,} ({int(max_w)}x{int(max_h)})"
    }
    log_config = _format_block(cfg_data)

    # --- Block 3: Result Info (Dict) ---
    res_data = {
        "Extracted Frames": str(len(frames)),
        "Final Input Size": f"{final_w} x {final_h}",
        "Final Pixels": f"{final_pixels:,} px",
        "Compression": f"{(final_pixels/orig_pixels)*100:.1f}% of original video"
    }
    log_result = _format_block(res_data)

    return [(img, f"Frame {i+1}\n{img.size}") for i, img in enumerate(resized)], log_source, log_config, log_result

# ==============================================================================
#  ADVANCED GEMINI SIMULATION LOGIC
# ==============================================================================

def _get_gemini_effective_max_edge(model_version, resolution_tier):
    """
    Reverse-engineers the 'Effective Resolution' based on Token Count tables.
    
    Logic:
    - If the model only uses 70 tokens, showing a 1080p image is misleading.
    - We simulate the 'Information Bottleneck' by downscaling to a resolution 
      that roughly matches the information content of the token count.
    """
    if "Gemini 3" in model_version:
        if resolution_tier == "High":
            # 280 Tokens -> Higher info density
            return 672  # Approx ~672x672 content
        else:
            # Low/Medium (70 Tokens) -> Low info density
            # This is roughly a thumbnail view
            return 336 
            
    elif "Gemini 2.5" in model_version:
        if resolution_tier == "Low":
            return 224  # 64 Tokens (Standard ViT input size)
        elif resolution_tier == "Medium":
            return 512  # 256 Tokens
        elif resolution_tier == "High":
            return 1024 # Pan & Scan / OCR support (High Res)
            
    # Default fallback
    return 512

def run_gemini_viz(video_name, resolution_tier, model_version):
    """
    Handler for Gemini Visualization with High-Fidelity Simulation.
    """
    # Defense
    forced_fps = 1.0
    
    # 1. Extract Frames
    frames, meta, error = _extract_logic(video_name, forced_fps)
    if error: return None, error, "", ""
    
    # 2. Determine Effective Resolution (The "Infinitely Close" Logic)
    target_max_edge = _get_gemini_effective_max_edge(model_version, resolution_tier)
    
    resized = []
    for f in frames:
        w, h = f.size
        # Calculate scaling factor to fit within target_max_edge
        # e.g., if image is 1920x1080 and target is 336:
        # scale = 336 / 1920 = 0.175
        ratio = target_max_edge / max(w, h)
        
        # Only downscale. Never upscale (if video is already small, keep it)
        if ratio < 1.0:
            new_w = int(w * ratio)
            new_h = int(h * ratio)
            resized.append(f.resize((new_w, new_h), Image.Resampling.BICUBIC))
        else:
            resized.append(f)
    
    # 3. Calculate Tokens (Exact Math from Docs)
    tokens_per_frame, total_tokens, guidance = _get_gemini_token_info(model_version, resolution_tier, len(frames))
    
    # --- Block 1: Source ---
    src_data = {
        "File Name": video_name,
        "Original FPS": f"{meta['orig_fps']:.2f}",
        "Original Size": str(meta['orig_res']),
        "Duration": f"{meta['duration']:.2f} sec"
    }
    log_source = _format_block(src_data)
    
    # --- Block 2: Config (Scientific Simulation) ---
    cfg_data = {
        "Model Family": model_version,
        "Resolution": resolution_tier,
        "Forced Target FPS": "1.0 FPS (fixed by Google)",
        "Effective Max Edge": f"{target_max_edge} px"
    }
    log_config = _format_block(cfg_data)
    
    # Add Technical Explanation
    log_config += f"\n----------------------------------------\nℹ️ SIMULATION LOGIC:\n• Based on {tokens_per_frame} tokens/frame\n• Max edge constrained to {target_max_edge}px\n  to mimic info bottleneck."
    
    # --- Block 3: Result ---
    final_res = resized[0].size
    res_data = {
        "Total Frames": str(len(frames)),
        "Tokens/Frame": str(tokens_per_frame),
        "Total Cost": f"{total_tokens:,} Tokens",
        "Simulated Input": f"{final_res[0]} x {final_res[1]} px"
    }
    log_result = _format_block(res_data)

    return [(img, f"Frame {i+1}\n{img.size}") for i, img in enumerate(resized)], log_source, log_config, log_result