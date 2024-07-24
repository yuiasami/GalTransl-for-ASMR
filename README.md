
<div align=center><img width="150" height="150" src="./img/logo.png"/></div>

<h1><p align='center' >GalTransl for ASMR</p></h1>
<div align=center><img src="https://img.shields.io/github/v/release/XD2333/GalTransl"/>   <img src="https://img.shields.io/github/license/XD2333/GalTransl"/>   <img src="https://img.shields.io/github/stars/XD2333/GalTransl"/></div>
<p align='center' >支持GPT3.5/4/Newbing等大语言模型的ASMR自动化翻译解决方案</p>
  
  GalTransl是一套将数个基础功能上的微小创新与对GPT提示工程（Prompt Engineering）的深度利用相结合的Galgame自动化翻译工具，用于制作内嵌式翻译补丁。 GalTransl for ASMR是GalTransl的一个分支，您可以使用本程序将日语音视频文件/字幕文件转换为中文字幕文件。

## GalTransl for ASMR 本地部署（Windows）

1. 创建环境：运行 `build_environment.bat`。如果你没有Python请在[微软商店](https://apps.microsoft.com/detail/9nrwmjp3717k)下载，请使用3.11及以上版本。脚本使用了国内镜像，如果是国外用户请删去bat文件第二行。

2. 运行GalTransl：运行 `run_web_demo.bat`，按照数字提示进行。

* Whisper模型会在第一次使用的时候自动下载，脚本使用了国内镜像，如果是国外用户请删去bat文件第一行。

* 输出的字幕会存在输入文件的目录，也可以在网页上下载，并且会在`sampleProject`目录进行备份。

## Galtransl for ASMR + Sakura 0.9b 离线翻译服务器部署（Linux）

您也可以使用docker创建一个虚拟机来构建整个离线翻译系统（约40G），请确认你已经安装[docker](https://www.docker.com/get-started/)和[nvidia-container-toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)。请运行以下命令：

```
sudo docker run --gpus all --ipc=host --network=host shinnpuru/galtransl_asmr:latest
```

然后访问`http://127.0.0.1:7860`即可开始翻译，翻译器请选择sakura0.9。

或者您可以从头开始构建docker镜像以使用最新的代码：

```
git clone https://github.com/shinnpuru/GalTransl-for-ASMR
cd GalTransl-for-ASMR
sudo docker build  -t galtransl_asmr  .
sudo docker run --gpus all --ipc=host --network=host galtransl_asmr
```
