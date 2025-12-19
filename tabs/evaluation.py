import os
import json
import traceback
from datetime import datetime
import config
from google import genai
from google.genai import types
import time
import utils
from dotenv import load_dotenv

load_dotenv()


def run_gemini_inference(
    username,
    task_name,
    model_name,
    video_name,
    prompt_list,
    resolution=None,
    thinking_level=None,
):
    """
    Real Gemini Inference Pipeline.
    1. Upload Video -> 2. Wait Process -> 3. Generate -> 4. Save
    """
    # --- 1. Basic Validation ---
    if not username:
        return "❌ Error: Not logged in."
    if not video_name:
        return "❌ Error: No video selected."
    if model_name.lower().startswith("gemini-2.5"):
        if resolution or thinking_level:
            yield "❌ Error: Gemini-2.5 models do not support resolution or thinking level settings."
            return
    if model_name.lower().startswith("gemini-3"):
        if not resolution or not thinking_level:
            yield "⚠️ Warning: Gemini-3 models recommend setting resolution and thinking level. Using defaults: Medium resolution, Low thinking."
            return

    final_prompt = utils.construct_structured_prompt(prompt_list)

    # Configure Gemini Client
    try:
        client = genai.Client(api_key=os.getenv("GOOGLE_AI_STUDIO_API_KEY"))
    except Exception as e:
        yield f"❌ Error: Failed to initialize Gemini Client.\n{str(e)} Please check your API key."
        return

    # Defaults
    if not task_name:
        task_name = "default_task"

    # --- 2. Prepare Save Paths ---
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Folder: model_results / Username / Model_Task_Timestamp
    session_id = f"{task_name.replace(' ', '')}_{timestamp}"
    save_dir = os.path.join(config.MODEL_RESULTS_DIR, username, session_id)
    os.makedirs(save_dir, exist_ok=True)

    status_log = []
    video_path = os.path.join(config.DATASET_DIR, video_name)

    if not os.path.exists(video_path):
        yield f"❌ Error: Video file not found at path: {video_path}"
        return

    def get_log_str():
        return "\n".join(status_log)

    try:
        # --- 3. Upload Video to Gemini File API ---
        status_log.append(f"📤 Uploading {video_name} to Google...")
        yield get_log_str()

        video_file = client.files.upload(file=video_path)

        status_log.append(f"✅ Uploaded. URI: {video_file.uri}")
        yield get_log_str()

        # --- 4. Wait for Processing ---
        status_log.append("⏳ Waiting for video processing...")
        yield get_log_str()

        while video_file.state == "PROCESSING":
            time.sleep(2)
            video_file = client.files.get(name=video_file.name)

        if video_file.state == "FAILED":
            raise ValueError("Video processing failed on Google side.")

        status_log.append("✅ Video is ready.")
        yield get_log_str()

        # --- 5. Generate Content ---
        status_log.append(f"🤖 Running Inference with {model_name}")
        yield get_log_str()

        # Using Gemini3
        if model_name.lower().startswith("gemini-3") and (
            resolution and thinking_level
        ):
            status_log.append(
                f"Runing Gemini-3 with Resolution: {resolution}, Thinking Level: {thinking_level}"
            )
            yield get_log_str()

            # Resolution & Thinking Config
            res_map = {
                "Low": "media_resolution_low",
                "Medium": "media_resolution_medium",
                "High": "media_resolution_high",
            }
            generate_content_config = types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(
                    thinking_level=thinking_level.upper()
                ),
                media_resolution=res_map.get(resolution, "media_resolution_medium"),
                response_mime_type="application/json",
            )

            # Generation
            response = client.models.generate_content(
                model=model_name.lower(),
                contents=[video_file, final_prompt],
                config=generate_content_config,
            )
        else:
            status_log.append(
                "Running Gemini-2.5 (or default) without special configs."
            )
            yield get_log_str()

            # Using Gemini 2.5
            response = client.models.generate_content(
                model=model_name.lower(),
                contents=[video_file, final_prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                ),
            )

        status_log.append("✅ Inference completed.")
        yield get_log_str()

        # --- 6. Parse Result ---
        status_log.append("📄 Parsing response...")
        yield get_log_str()

        # Assume response.text contains JSON string
        raw_text = response.text
        try:
            parsed_data = json.loads(raw_text)
        except json.JSONDecodeError:
            # Fallback: sometimes model adds ```json ... ``` wrapper
            try:
                cleaned_text = (
                    raw_text.replace("```json", "").replace("```", "").strip()
                )
                parsed_data = json.loads(cleaned_text)
            except json.JSONDecodeError:
                status_log.append(f"⚠️ JSON Parse Failed. Raw Text:\n{raw_text}")
                raise ValueError("Failed to parse model response as JSON.")

        status_log.append("✅ Response parsed successfully.")
        yield get_log_str()

        # --- 7. Save Files ---
        status_log.append("💾 Saving results...")
        yield get_log_str()

        # File A: Prediction
        pred_path = os.path.join(save_dir, "model_predict.json")
        with open(pred_path, "w", encoding="utf-8") as f:
            json.dump(parsed_data, f, indent=4, ensure_ascii=False)

        # File B: Metadata
        useage = response.usage_metadata
        token_usage = {
            "input_tokens": useage.prompt_token_count if useage else 0,
            "output_tokens": useage.candidates_token_count if useage else 0,
            "thinking_tokens": useage.thoughts_token_count if useage else 0,
            "total_tokens": useage.total_token_count if useage else 0,
        }

        # Save API Usage Log
        utils.update_api_usage(username, model_name, token_usage)

        meta_path = os.path.join(save_dir, "metadata.json")
        meta_data = {
            "user": username,
            "model_name": model_name,
            "task": task_name,
            "video": video_name,
            "fps_setting": "1.0",  # Fixed by Google
            "resolution_setting": (
                resolution if resolution else "Default for Gemini-2.5"
            ),
            "thinking_level": (
                thinking_level if thinking_level else "Default for Gemini-2.5"
            ),
            "prompt": final_prompt,
            "timestamp": timestamp,
            "gemini_file_uri": video_file.uri,
            "token_usage": token_usage,
            "estimated_cost_usd": utils.calculate_cost(
                model_name,
                token_usage["input_tokens"],
                token_usage["output_tokens"] + token_usage["thinking_tokens"],
            ),
        }
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta_data, f, indent=4, ensure_ascii=False)

        status_log.append(f"💾 Saved to: {pred_path}")
        status_log.append(
            f"📊 Token Usage: Input={token_usage['input_tokens']}, Thinking={token_usage['thinking_tokens']}, Output={token_usage['output_tokens']}, Total={token_usage['total_tokens']}"
        )
        yield get_log_str()

        # Cleanup Google File (Optional, good practice to save storage)
        # genai.delete_file(video_file.name)

    except Exception as e:
        tb_str = traceback.format_exc()
        status_log.append(f"❌ Critical Error:\n{str(e)}\n\nTraceback:\n{tb_str}")
        yield get_log_str()


def run_gemini_inference_mock(
    username, task_name, model_name, video_name, fps, resolution, prompt
):
    """
    Simulates Inference.
    Structure: model_results/{Username}/{Model}_{Task}_{Time}/
    """
    if not username:
        return "❌ Error: Not logged in."
    if not video_name:
        return "❌ Error: No video selected."

    # Defaults
    if not task_name:
        task_name = "task"
    if not model_name:
        model_name = "Gemini"

    # 1. Create Session ID (Folder Name)
    # Sanitize inputs to be folder-safe
    safe_model = model_name.replace(" ", "-")
    safe_task = task_name.replace(" ", "-")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    session_id = f"{safe_model}_{safe_task}_{timestamp}"

    # 2. Path: model_results / Username / SessionID
    save_dir = os.path.join(config.MODEL_RESULTS_DIR, username, session_id)
    os.makedirs(save_dir, exist_ok=True)

    # 3. Generate Mock Data
    mock_data = [
        {
            "start_time": "00:00:00",
            "end_time": "00:00:05",
            "behavior": "interaction",
            "confidence": 0.92,
            "description": f"Mock prediction for {video_name}.",
        }
    ]

    # 4. Save Standardized Files
    # File A: The Prediction
    pred_path = os.path.join(save_dir, "model_predict.json")
    with open(pred_path, "w", encoding="utf-8") as f:
        json.dump(mock_data, f, indent=4)

    # File B: The Metadata
    meta_path = os.path.join(save_dir, "metadata.json")
    meta_data = {
        "user": username,
        "model": model_name,
        "task": task_name,
        "video": video_name,
        "fps": fps,
        "resolution": resolution,
        "prompt": prompt,
        "timestamp": timestamp,
    }
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta_data, f, indent=4)

    return (
        f"✅ Done!\nSaved to:\n{save_dir}\n(Files: model_predict.json, metadata.json)"
    )
