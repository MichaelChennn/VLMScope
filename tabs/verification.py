import os
import json
import subprocess
import traceback
import imageio_ffmpeg
import gradio as gr
from datetime import datetime
import config
import utils


def cut_video(video_name, start_sec, end_sec, segment_id):
    """Cuts a video segment using ffmpeg (re-encoding for accuracy)."""
    if not video_name:
        return None
    video_path = os.path.join(config.DATASET_DIR, video_name)

    output_path = os.path.join(config.TEMP_DIR, f"clip_{segment_id}.mp4")

    # Simple caching: return if exists
    if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
        return output_path

    try:
        ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
        duration = end_sec - start_sec
        cmd = [
            ffmpeg_exe,
            "-y",
            "-ss",
            str(start_sec),
            "-i",
            video_path,
            "-t",
            str(duration),
            "-c:v",
            "libx264",
            "-preset",
            "ultrafast",
            "-c:a",
            "aac",
            "-strict",
            "experimental",
            output_path,
        ]
        subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"❌ FFmpeg Process Error: {e.stderr.decode() if e.stderr else str(e)}")
        return None
    except Exception as e:
        print(f"❌ Error cutting video: {str(e)}\n{traceback.format_exc()}")
        return None


def load_data(video_name, input_mode, raw_json, selected_file):
    """
    Loads JSON result and Metadata.
    Returns: (DropdownUpdate, DataState, StatusMsg, PromptText)
    """
    utils.cleanup_temp_folder()

    json_content = ""
    prompt_text = "⚠️ No metadata found."  # 默认值

    if input_mode == "Paste Raw JSON":
        json_content = raw_json
        prompt_text = "N/A (Raw JSON input)"
    else:
        if not selected_file:
            return gr.update(choices=[]), [], "❌ No file selected.", ""

        # 1. Load Result JSON
        full_path = os.path.join(config.MODEL_RESULTS_DIR, selected_file)
        if os.path.exists(full_path):
            with open(full_path, "r", encoding="utf-8") as f:
                json_content = f.read()

            # 2. Load Metadata for Prompt
            result_dir = os.path.dirname(full_path)
            meta_path = os.path.join(result_dir, "metadata.json")

            if os.path.exists(meta_path):
                try:
                    with open(meta_path, "r", encoding="utf-8") as mf:
                        meta_data = json.load(mf)
                        prompt_text = meta_data.get(
                            "prompt", "Prompt field missing in metadata."
                        )

                except Exception as e:
                    prompt_text = f"❌ Error reading metadata: {str(e)}"
                    print(f"Metadata Error Traceback:\n{traceback.format_exc()}")
        else:
            return gr.update(choices=[]), [], "❌ File not found.", ""

    if not json_content.strip():
        return gr.update(choices=[]), [], "❌ Empty JSON.", ""

    try:
        valid_json = utils.fix_json_format(json_content)
        data = json.loads(valid_json)
    except json.JSONDecodeError as e:
        return gr.update(choices=[]), [], f"❌ JSON Error: {e}", ""
    except Exception as e:
        tb = traceback.format_exc()
        return (
            gr.update(choices=[]),
            [],
            f"❌ Unexpected Error loading JSON: {str(e)}",
            "",
        )

    choices = []
    parsed_data = []
    for idx, item in enumerate(data):
        item["human_label"] = None
        item["human_comment"] = ""
        start = item.get("start_time", "00:00:00")
        end = item.get("end_time", "00:00:00")
        label = item.get("behavior", item.get("emotion", "Unknown"))
        choices.append(f"{idx+1}. {start}-{end} | {label}")
        parsed_data.append(item)

    return (
        gr.update(choices=choices, value=choices[0] if choices else None),
        parsed_data,
        f"✅ Loaded {len(data)} items.",
        prompt_text,
    )


def update_ui(choice, all_data, video_name):
    """Updates the video player and details based on dropdown selection."""
    # if not choice or not all_data: return None, "", "", "", "Unlabeled"

    # try: idx = int(choice.split(".")[0]) - 1
    # except: return None, "", "", "", "Error"

    if not choice or not all_data:
        return None, "", "", "⚪ Unlabeled"

    try:
        idx = int(choice.split(".")[0]) - 1
    except Exception as e:
        print(f"❌ Error parsing index from choice '{choice}': {e}")
        return None, "", "", "Error parsing index"

    item = all_data[idx]

    # Parse time
    s_sec = utils.time_str_to_seconds(item.get("start_time", "00:00:00"))
    e_sec = utils.time_str_to_seconds(item.get("end_time", "00:00:00"))
    if e_sec <= s_sec:
        e_sec = s_sec + 1

    # Cut video
    clip = cut_video(video_name, s_sec, e_sec, idx)

    # Display details
    json_pretty = json.dumps(item, indent=4, ensure_ascii=False)
    md = f"### Segment {idx+1}\n\n```json\n{json_pretty}\n```"

    # Update status text
    hl = item.get("human_label")
    st = "⚪ Unlabeled"
    if hl is True:
        st = "✅ TRUE"
    elif hl is False:
        st = "❌ FALSE"
    elif hl == "not_sure":
        st = "⚠️ NOT SURE"

    return clip, md, item.get("human_comment", ""), st


def handle_label(choice, all_data, comment, val):
    """Saves the user label to memory and advances to the next segment."""
    try:
        idx = int(choice.split(".")[0]) - 1
    except Exception as e:
        print(f"❌ Error parsing index in handle_label: {e}")
        return all_data, f"Error: {str(e)}", choice

    all_data[idx]["human_label"] = val
    all_data[idx]["human_comment"] = comment

    msg_map = {
        True: "Saved: TRUE",
        False: "Saved: FALSE",
        "not_sure": "Saved: NOT SURE",
    }
    msg = msg_map.get(val, "Saved")

    next_idx = idx + 1
    if next_idx < len(all_data):
        item = all_data[next_idx]
        start = item.get("start_time", "00:00:00")
        end = item.get("end_time", "00:00:00")
        label = item.get("behavior", item.get("emotion", "Unknown"))
        next_choice = f"{next_idx+1}. {start}-{end} | {label}"
        return all_data, f"✅ {msg}", next_choice
    else:
        return all_data, f"✅ {msg} (End of List)", choice


def save_file(data, current_user, video_name, source_rel_path):
    """
    Saves to human_results using the EXACT SAME folder structure as model_results.
    Handles multiple saves by timestamping.
    """
    if not data:
        return "No Data."
    if not current_user:
        return "❌ Not logged in."

    # 1. Determine Target Directory (Mirroring)
    # source_rel_path e.g.: "Alice/Gemini_Task1_2025/model_predict.json"

    target_folder = ""

    if source_rel_path:
        # Get the directory part: "Alice/Gemini_Task1_2025"
        # This keeps the original Creator and Session ID
        target_folder = os.path.dirname(source_rel_path)
    else:
        # Fallback for manual copy-paste
        target_folder = (
            f"{current_user}/Manual_Upload_{datetime.now().strftime('%Y%m%d')}"
        )

    # Full path: human_results / Alice / Gemini_Task1_2025 /
    full_target_dir = os.path.join(config.HUMAN_RESULTS_DIR, target_folder)
    os.makedirs(full_target_dir, exist_ok=True)

    # 2. Construct Filename (Versioning)
    # human_predict_Verifier_Timestamp.json
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"human_predict_{current_user}_{timestamp}.json"
    save_path = os.path.join(full_target_dir, filename)

    # 3. Stats & Content
    tc = sum(1 for x in data if x.get("human_label") == True)
    fc = sum(1 for x in data if x.get("human_label") == False)
    nc = sum(1 for x in data if x.get("human_label") == "not_sure")

    final_output = {
        "summary_statistics": {
            "true": tc,
            "false": fc,
            "not_sure": nc,
            "total": len(data),
            "video_path": video_name,  # 🟢 Added as requested
        },
        "meta": {
            "verified_by": current_user,
            "source_file": source_rel_path,
            "timestamp": datetime.now().isoformat(),
        },
        "data": data,
    }

    try:
        with open(save_path, "w", encoding="utf-8") as f:
            json.dump(final_output, f, indent=4, ensure_ascii=False)
        return f"✅ Saved to:\n.../{target_folder}/\n{filename}"
    except Exception as e:
        tb = traceback.format_exc()
        return f"❌ Error saving file: {str(e)}\nTraceback:\n{tb}"


def save_comment(choice, all_data, txt):
    """Updates the comment in memory as the user types."""
    try:
        idx = int(choice.split(".")[0]) - 1
    except Exception:
        return all_data
    if idx >= 0:
        all_data[idx]["human_comment"] = txt
    return all_data
