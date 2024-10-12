
<div align=center><img width="150" height="150" src="./img/logo.png"/></div>

<h1><p align='center' >GalTransl for ASMR</p></h1>
<div align=center><img src="https://img.shields.io/github/v/release/XD2333/GalTransl"/>   <img src="https://img.shields.io/github/license/XD2333/GalTransl"/>   <img src="https://img.shields.io/github/stars/XD2333/GalTransl"/></div>
<p align='center' >支持GPT3.5/4/Newbing等大语言模型的ASMR自动化翻译解决方案</p>
  
  GalTransl是一套将数个基础功能上的微小创新与对GPT提示工程（Prompt Engineering）的深度利用相结合的Galgame自动化翻译工具，用于制作内嵌式翻译补丁。 GalTransl for ASMR是GalTransl的一个分支，您可以使用本程序将日语音视频文件/字幕文件转换为中文字幕文件。

## 特色

* 支持多种翻译模型，包括在线模型（GPT3.5、GPT4、Moonshot、Minimax、Qwen、GLM）和本地模型（Sakura、Index、Galtransl）等。
* 支持AMD/NVIDIA/Intel GPU加速，翻译引擎支持CPU/GPU混合运行，具体支持的GPU请参考[whisper.cpp](https://github.com/Const-me/Whisper)和[llama.cpp](https://github.com/ggerganov/llama.cpp)。
* 支持多种输入格式，包括音频、视频、SRT字幕。
* 支持多种输出格式，包括SRT字幕、LRC字幕。
* 支持字典功能，可以自定义翻译字典，替换输入输出。
* 支持从YouTube/Bilibili直接下载视频。
* 支持文件和链接批量处理，自动识别文件类型。

## 使用

1. 创建环境：运行 `build_environment.bat`。如果你没有Python请在[微软商店](https://apps.microsoft.com/detail/9nrwmjp3717k)下载，请使用3.11及以上版本。脚本使用了国内镜像，如果是国外用户请删去bat文件第二行。

2. 启动：运行 `run_web_demo.bat`，按照数字提示进行，可以只利用听写或者翻译功能。

* 听写模型基于[whisper.cpp](https://github.com/Const-me/Whisper)引擎，需要自行下载，请选择合适的模型下载然后放到`whisper`文件夹下。

| 模型  | 磁盘    | 显存     | 链接 |
| ------ | ------- | ------- | ----- |
| small  | 466 MiB | ~852 MB | [下载](https://hf-mirror.com/ggerganov/whisper.cpp/resolve/main/ggml-small.bin?download=true) |
| medium | 1.5 GiB | ~2.1 GB | [下载](https://hf-mirror.com/ggerganov/whisper.cpp/resolve/main/ggml-medium.bin?download=true) |
| large  | 2.9 GiB | ~3.9 GB | [下载](https://hf-mirror.com/ggerganov/whisper.cpp/resolve/main/ggml-large-v2.bin?download=true) |

* 本地翻译模型基于[llama.cpp](https://github.com/ggerganov/llama.cpp)引擎，需要自行下载，可以参考[GalTransl](https://github.com/xd2333/GalTransl)，[Index](https://github.com/bilibili/Index-1.9B)，[Sakura](https://github.com/SakuraLLM/SakuraLLM)等项目，仅支持`.gguf`格式的模型。

| 模型  | 磁盘    | 显存     | 链接 |
| ------ | ------- | ------- | ----- |
| Index-1.9B-Q4  | 1.24 MiB | ~4G | [下载](https://hf-mirror.com/IndexTeam/Index-1.9B-Chat-GGUF/resolve/main/ggml-model-Q4_K_M.gguf?download=true) |
| Sakura-7B-Q4  | 4.56 GiB | ~8 GB | [下载](https://hf-mirror.com/SakuraLLM/Sakura-7B-LNovel-v0.9-GGUF/resolve/main/sakura-7b-lnovel-v0.9-Q4_K_M.gguf?download=true) |
| GalTransl-7B-Q6 | 5.9 GiB | ~8 GB | [下载](https://hf-mirror.com/SakuraLLM/GalTransl-7B-v2.5/resolve/main/GalTransl-7B-v2-Q6_K.gguf?download=true) |
| Sakura-13B-Q4  | 9.45 GB | ~16 GB | [下载](https://hf-mirror.com/SakuraLLM/Sakura-14B-LNovel-v0.9b-GGUF/resolve/main/sakura-13b-lnovel-v0.9b-Q4_K_M.gguf?download=true) |

* 输入的文件和输出的字幕会存在`project/cache`目录，可以通过网页一键清理。

## 声明

本软件仅供学习交流使用，不得用于商业用途。本软件不对任何使用者的行为负责，不保证翻译结果的准确性。使用本软件即代表您同意自行承担使用本软件的风险，包括但不限于版权风险、法律风险等。请遵守当地法律法规，不要使用本软件进行任何违法行为。
