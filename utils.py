import os
import re
import shutil
from datetime import datetime, timedelta
import config  # Import global config
import json

def get_video_files():
    """Scans the dataset folder for video files."""
    if not os.path.exists(config.DATASET_DIR):
        return []
    # Filter for common video extensions
    files = [f for f in os.listdir(config.DATASET_DIR) if f.lower().endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    return sorted(files) if files else []

def get_model_result_files():
    """
    Scans model_results and lists ONLY 'model_predict.json' files.
    Returns relative paths like: "Alice/Gemini_Task1_2025/model_predict.json"
    """
    json_files = []
    if not os.path.exists(config.MODEL_RESULTS_DIR):
        return []
    
    for root, dirs, files in os.walk(config.MODEL_RESULTS_DIR):
        for file in files:
            # Only include 'model_predict.json'
            if file == "model_predict.json":
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, config.MODEL_RESULTS_DIR)
                json_files.append(rel_path)
    
    # Sort: Newest folders usually have larger timestamp numbers, so reverse sort works well
    return sorted(json_files, reverse=True)

def cleanup_temp_folder():
    """Deletes all files in the temp_clips folder."""
    if os.path.exists(config.TEMP_DIR):
        for filename in os.listdir(config.TEMP_DIR):
            file_path = os.path.join(config.TEMP_DIR, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

def time_str_to_seconds(time_str):
    """Converts 'HH:MM:SS' string to total seconds (float)."""
    try:
        t = datetime.strptime(time_str.strip(), "%H:%M:%S")
        delta = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
        return delta.total_seconds()
    except ValueError:
        return 0.0

def fix_json_format(json_str):
    """
    Robust JSON fixer using Regex.
    Handles concatenated objects (e.g., } {) missing commas.
    """
    json_str = json_str.strip()
    
    # Regex: Find '}' followed by optional whitespace and '{', replace with '}, {'
    json_str = re.sub(r'\}\s*\{', '}, {', json_str)
    
    # Wrap in brackets if missing
    if not json_str.startswith("["): 
        json_str = f"[{json_str}]"
    
    # Remove trailing commas before closing bracket
    json_str = re.sub(r',\s*\]', ']', json_str)
    
    return json_str

def get_gemini_models():
    return config.GEMINI_MODELS

# ==============================================================================
#  API USAGE & COST LOGIC
# ==============================================================================

def _identify_model_family(model_name):
    """Helper to match model string to pricing key."""
    name = model_name.lower()
    if "gemini-3" in name: return "gemini-3"
    if "gemini-2" in name: return "gemini-2"
    if "gemini-1.5" in name: return "gemini-1.5"
    return "gemini-2" # Default fallback

def calculate_cost(model_name, input_tokens, output_tokens):
    """
    Calculates cost in USD based on context length tier.
    Pricing is per 1,000,000 tokens.
    """
    family = _identify_model_family(model_name)
    rates = config.PRICING_TABLE.get(family, config.PRICING_TABLE["gemini-2"])
    
    # Context Tier Logic (Threshold: 200k)
    # Usually tier is determined by Input + Output context window, 
    # but for simplicity we usually check input length or total. 
    # Google standard: prompt length determines input tier.
    is_high_context = input_tokens > 200000
    
    price_in = rates["input_high"] if is_high_context else rates["input_low"]
    price_out = rates["output_high"] if is_high_context else rates["output_low"]
    
    cost_in = (input_tokens / 1_000_000) * price_in
    cost_out = (output_tokens / 1_000_000) * price_out
    
    return round(cost_in + cost_out, 6)

def update_api_usage(username, model_name, token_dict):
    """
    Updates api_usage.json with new token counts.
    Structure: { Username: { ModelName: { input, output, thinking, total, cost, last_updated } } }
    """
    if not username: return
    
    # 1. Load existing data
    data = {}
    if os.path.exists(config.API_USAGE_FILE):
        try:
            with open(config.API_USAGE_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            data = {}

    # 2. Init User/Model if not exist
    if username not in data:
        data[username] = {}
    if model_name not in data[username]:
        data[username][model_name] = {
            "input_tokens": 0,
            "output_tokens": 0,
            "thinking_tokens": 0,
            "total_tokens": 0,
            "total_cost_usd": 0.0,
            "last_updated": ""
        }
    
    # 3. Calculate Cost for THIS transaction
    current_cost = calculate_cost(
        model_name, 
        token_dict.get("input_tokens", 0), 
        token_dict.get("output_tokens", 0) + token_dict.get("thinking_tokens", 0)
    )

    # 4. Update Accumulators
    record = data[username][model_name]
    record["input_tokens"] += token_dict.get("input_tokens", 0)
    record["output_tokens"] += token_dict.get("output_tokens", 0)
    record["thinking_tokens"] += token_dict.get("thinking_tokens", 0)
    record["total_tokens"] += token_dict.get("total_tokens", 0)
    record["total_cost_usd"] += current_cost
    record["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 5. Save
    with open(config.API_USAGE_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def get_usage_summary():
    """
    Returns a list of lists for Gradio Dataframe.
    [User, Model, Input, Output, Thinking, Total, Cost($), Last Active]
    """
    if not os.path.exists(config.API_USAGE_FILE):
        return []
    
    try:
        with open(config.API_USAGE_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except:
        return []

    summary = []
    for user, models in data.items():
        for model, stats in models.items():
            summary.append([
                user,
                model,
                stats["input_tokens"],
                stats["output_tokens"],
                stats["thinking_tokens"],
                stats["total_tokens"],
                f"${stats['total_cost_usd']:.4f}",
                stats["last_updated"]
            ])
            
    # Sort by User then Model
    summary.sort(key=lambda x: (x[0], x[1]))
    return summary

# ==============================================================================
#  PROMPT ENGINEERING HELPERS
# ==============================================================================
def construct_structured_prompt(prompt_parts):
    """
    Assembles 6 parts into a single formatted prompt string.
    """
    headers = [
        "Background Introduction",
        "Task Description",
        "Label Identify",
        "Condition Evaluation",
        "Evidence",
        "Output Example"
    ]
    
    formatted_parts = []
    
    for header, content in zip(headers, prompt_parts):
        if content and str(content).strip():
            formatted_parts.append(f"{header}:\n{str(content).strip()}")
    
    return "\n\n".join(formatted_parts)