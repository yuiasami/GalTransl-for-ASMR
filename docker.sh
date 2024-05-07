cd /app/Sakura-13B-Galgame
python server.py --model_name_or_path sakura-13b-lnovel-v0.9b-Q4_K_M.gguf --llama_cpp --use_gpu --model_version 0.9 --trust_remote_code --no-auth --listen 127.0.0.1:8080 >log 2>&1 &
cd /app/GalTransl-for-ASMR 
python app.py
