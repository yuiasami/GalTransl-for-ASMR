# This is the main entry of the program. You can run this file to start the program.
from command import BulletMenu

print("欢迎使用GalTransl for ASMR！")

print("您可以使用本程序将日语音频文件转换为字幕文件。")

input_file = input("请输入音频文件/SRT文件路径（或拖拽文件到窗口）：").strip('"')

if input_file.endswith('.srt'):
    print("正在进行字幕转换...")
    from srt2prompt import make_prompt

    import os
    output_file_path = os.path.join('sampleProject/gt_input', os.path.basename(input_file).replace('.srt','.json'))

    make_prompt(input_file, output_file_path)
    print("字幕转换完成！")

else:
    import os
    os.system("")
    model_size = BulletMenu(
        "请选择语音识别模型大小:（默认为large-v3）", {'large-v3': "大模型，约5G显存", 'small':"小模型，约2G显存", 'medium':"中模型，约3G显存"}
    ).run(0)

    print("正在进行语音识别...")
    from whisper2prompt import execute_asr
    output_file_path = execute_asr(
        input_file  = input_file,
        output_folder = 'sampleProject/gt_input',
        model_size    = model_size,
        language      = 'ja',
        precision     = 'float16',
    )


project_dir, config_file_name = 'sampleProject', 'config.yaml'
from GalTransl import TRANSLATOR_SUPPORTED
translator = BulletMenu(
    f"请选择翻译器：", TRANSLATOR_SUPPORTED
).run(0)


print("正在进行翻译...")
from GalTransl.__main__ import worker
worker(project_dir, config_file_name, translator, show_banner=False)

print("正在生成字幕文件...")
from prompt2srt import make_srt
make_srt(output_file_path.replace('gt_input','gt_output'), input_file+'.srt')

input("按任意键退出...")