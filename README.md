
<div align=center><img width="150" height="150" src="./img/logo.png"/></div>

<h1><p align='center' >GalTransl for ASMR</p></h1>
<div align=center><img src="https://img.shields.io/github/v/release/XD2333/GalTransl"/>   <img src="https://img.shields.io/github/license/XD2333/GalTransl"/>   <img src="https://img.shields.io/github/stars/XD2333/GalTransl"/></div>
<p align='center' >支持GPT3.5/4/Newbing等大语言模型的ASMR自动化翻译解决方案</p>
  
  GalTransl是一套将数个基础功能上的微小创新与对GPT提示工程（Prompt Engineering）的深度利用相结合的Galgame自动化翻译工具，用于制作内嵌式翻译补丁。 GalTransl for ASMR是GalTransl的一个分支，您可以使用本程序将日语音视频文件/字幕文件转换为中文字幕文件。

## 特色

* 支持多种翻译模型，包括在线模型（GPT3.5、GPT4、Moonshot、Minimax、Qwen、GLM）和本地模型（Sakura、Index、Galtransl）等。
* 支持多种输入格式，包括音频、视频、SRT字幕。
* 支持多种输出格式，包括SRT字幕、LRC字幕。
* 支持字典功能，可以自定义翻译字典，替换输入输出。
* 支持从YouTube/Bilibili直接下载视频。
* 支持文件和链接批量处理，自动识别文件类型。

## 使用

1. 创建环境：运行 `build_environment.bat`。如果你没有Python请在[微软商店](https://apps.microsoft.com/detail/9nrwmjp3717k)下载，请使用3.11及以上版本。脚本使用了国内镜像，如果是国外用户请删去bat文件第二行。

2. 启动：运行 `run_web_demo.bat`，按照数字提示进行。

* 听写模型（Faster-Whisper）模型会在第一次使用的时候自动下载，脚本使用了国内镜像，如果是国外用户请删去bat文件第一行。

* 本地翻译模型需要自行下载，可以在[GalTransl](https://github.com/xd2333/GalTransl)，[Index](https://github.com/bilibili/Index-1.9B)，[Sakura](https://github.com/SakuraLLM/SakuraLLM)等项目中下载，仅支持GGUF格式的模型。

* 输入的文件和输出的字幕会存在`sampleProject/cache`目录，可以通过网页一键清理。

## 声明

本软件仅供学习交流使用，不得用于商业用途。本软件不对任何使用者的行为负责，不保证翻译结果的准确性。使用本软件即代表您同意自行承担使用本软件的风险，包括但不限于版权风险、法律风险等。请遵守当地法律法规，不要使用本软件进行任何违法行为。
