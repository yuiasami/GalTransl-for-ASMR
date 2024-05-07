FROM nvcr.io/nvidia/pytorch:23.07-py3

EXPOSE 7860

ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN mkdir /app

WORKDIR /app
RUN git clone -b v0.2 https://github.com/shinnpuru/GalTransl-for-ASMR

WORKDIR /app/GalTransl-for-ASMR
RUN pip config set global.index-url https://mirror.sjtu.edu.cn/pypi/web/simple
RUN pip install -r requirements.txt

RUN pip install "huggingface_hub[cli]"
ENV HF_ENDPOINT=https://hf-mirror.com
RUN huggingface-cli download  --resume-download Systran/faster-whisper-small
RUN huggingface-cli download  --resume-download Systran/faster-whisper-medium
RUN huggingface-cli download  --resume-download Systran/faster-whisper-large-v3

WORKDIR /app
RUN git clone -b b192 https://github.com/SakuraLLM/Sakura-13B-Galgame

WORKDIR /app/Sakura-13B-Galgame
ENV CMAKE_ARGS="-DLLAMA_CUDA=on"
RUN pip install -r requirements.llamacpp.txt
RUN huggingface-cli download  --resume-download SakuraLLM/Sakura-13B-LNovel-v0.9b-GGUF sakura-13b-lnovel-v0.9b-Q4_K_M.gguf --local-dir .

WORKDIR /app/GalTransl-for-ASMR
CMD bash docker.sh
