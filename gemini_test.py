from google import genai
from google.genai import types
import os
import time
from dotenv import load_dotenv
load_dotenv()


client = genai.Client(api_key=os.getenv("GOOGLE_AI_STUDIO_API_KEY"))

video_path = "dataset/demo.mp4"

video_file = client.files.upload(
    file=video_path,
    config=types.UploadFileConfig(display_name="Demo Video")
)

print("正在等待视频处理...", end="")
while video_file.state.name == "PROCESSING":
    print(".", end="", flush=True)
    time.sleep(2) # 每2秒检查一次
    # 刷新文件状态
    video_file = client.files.get(name=video_file.name)

print(f"\n当前状态: {video_file.state.name}")

# 如果处理失败，抛出异常
if video_file.state.name != "ACTIVE":
    raise Exception(f"视频处理失败，状态: {video_file.state.name}")

res_map = {
        "Low": "media_resolution_low",
        "Medium": "media_resolution_medium",
        "High": "media_resolution_high"
    }
generate_content_config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_level="Low"),
    media_resolution="media_resolution_low",
    response_mime_type="application/json"
)
        
response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents=[video_file, "Describe the video in detail. Output the result in JSON format."],
    config=generate_content_config
)

print(response)
print("Response Text:")
print(response.text)

usage = response.usage_metadata
print(f"输入 Tokens:  {usage.prompt_token_count}")
print(f"输出 Tokens:  {usage.candidates_token_count}")
print(f"思考 Tokens:  {usage.thoughts_token_count}")
print(f"总计 Tokens:  {usage.total_token_count}")
# 2379

# To run this code you need to install the following dependencies:
# pip install google-genai

# from google import genai

# client = genai.Client(api_key=os.getenv("GOOGLE_AI_STUDIO_API_KEY"))

# response = client.models.generate_content(
#     model="gemini-3-pro-preview",
#     contents="Explain how AI works in a few words",
# )

# print(response)
# print("Response Text:")
# print(response.text)
