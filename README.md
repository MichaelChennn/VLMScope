# Environment

## Prepare the environment
- For Windows
```bash
conda create -n vlmscope python=3.10 -y
conda activate vlmscope
pip install -r requirements.txt
```
- For Mac
```bash
conda create -n vlmscope python=3.10 -y
conda activate vlmscope
pip install -r requirements_mac.txt
```

## Add Your Google AI Studio API keys
Create a `.env` file in the root directory and add your API keys as follows:

```
GOOGLE_AI_STUDIO_API_KEY=your_google_api_key
```

## Put the video files in the dataset folder
Place your video files in the `dataset/` directory. You can use the provided `demo1.mp4` or `demo2.mp4` for testing.

## Change the example prompts if needed
You can modify the example prompts in the `config.py` file (search "PROMPTS_EXAMPLES") to suit your evaluation needs.

## Run the application
```bash
python app.py
```

## How to use the application
Please refer to the [instruction.md](instruction.md) file for a detailed guide on how to use the application.

## File Structure
`dataset/`
- Store video files for evaluation

`human_results/` 
- Store human verification (True or False) results in subfolders with username

`model_results/` 
- Store model evaluation results in subfolders with username, model names and timestamps

`tabs/`
- Contains python files for logic for each tab in the app

`ui/`
- Contains python files for UI for each tab in the app

`temp_clips/`
- Temporary storage for video clips during processing, automatically cleared after use

`.env`
- Store environment variables such as API keys

`api_usage.json`
- Log file to track API usage statistics, you can copy it for backup

`app.py`
- Main application file to run the app




