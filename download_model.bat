.\venv\Scripts\python.exe -m pip install huggingface_hub
set HF_ENDPOINT=https://hf-mirror.com
rem .\venv\Scripts\huggingface-cli.exe download --resume-download Systran/faster-whisper-large-v3
rem .\venv\Scripts\huggingface-cli.exe download --resume-download Systran/faster-whisper-medium
.\venv\Scripts\huggingface-cli.exe download --resume-download Systran/faster-whisper-small
pause