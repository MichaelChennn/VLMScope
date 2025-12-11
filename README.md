# Environment

## Prepare the environment

```bash
conda create -n vlmscope python=3.10 -y
conda activate vlmscope
pip install -r requirements.txt
```

## Add Your Google AI Studio API keys
Create a `.env` file in the root directory and add your API keys as follows:

```
GOOGLE_AI_STUDIO_API_KEY=your_google_api_key
```

## Put the video files in the dataset folder
Place your video files in the `dataset/` directory. You can use the provided `demo.mp4` for testing.

## Run the application
```bash
python app.py
```
