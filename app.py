# follow main.py to create a web-based demo
import sys, os
sys.path.append(os.path.dirname(__file__))
import gradio as gr

def worker(input_file, model_size, translator, gpt_token, moonshot_token, sakura_address, proxy_address):
    if input_file.endswith('.srt'):
        from srt2prompt import make_prompt
        print("正在进行字幕转换...")
        import os
        output_file_path = os.path.join('sampleProject/gt_input', os.path.basename(input_file).replace('.srt','.json'))

        make_prompt(input_file, output_file_path)
        print("字幕转换完成！")
    else:
        import os
        print("正在进行语音识别...")
        from whisper2prompt import execute_asr
        output_file_path = execute_asr(
            input_file  = input_file,
            output_folder = 'sampleProject/gt_input',
            model_size    = model_size,
            language      = 'ja',
            precision     = 'float16',
        )
        print("语音识别完成！")

    print("正在进行翻译配置...")
    with open('sampleProject/config.yaml', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines):
        if gpt_token:
            if 'GPT35' in line:
                lines[idx+2] = f"      - token: {gpt_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://api.openai.com\n"
                lines[idx+7] = f'    rewriteModelName: ""\n'
            if 'GPT4' in line:
                lines[idx+2] = f"      - token: {gpt_token}\n"
        if moonshot_token:
            if 'GPT35' in line:
                lines[idx+4] = f"      - token: {moonshot_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://api.moonshot.cn\n"
                lines[idx+7] = f'    rewriteModelName: "moonshot-v1-8k"\n'
        if sakura_address:
            if 'Sakura' in line:
                lines[idx+1] = f"    endpoint: {sakura_address}\n"
        if proxy_address:
            if 'proxy' in line:
                lines[idx+1] = f"  enableProxy: true\n"
                lines[idx+3] = f"    - address: {proxy_address}\n"
        else:
            if 'proxy' in line:
                lines[idx+1] = f"  enableProxy: false\n"

    with open('sampleProject/config.yaml', 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("正在进行翻译...")
    from GalTransl.__main__ import worker
    worker('sampleProject', 'config.yaml', translator, show_banner=False)

    print("正在生成字幕文件...")
    from prompt2srt import make_srt, make_lrc
    make_srt(output_file_path.replace('gt_input','gt_output'), input_file+'.srt')
    make_lrc(output_file_path.replace('gt_input','gt_output'), input_file+'.lrc')
    print("字幕文件生成完成！")
    print("输入输出缓存地址为：", os.path.dirname(input_file))
    return input_file+'.srt', input_file+'.lrc'

def cleaner(input_file, output_srt, output_lrc):
    print("正在清理输入...")
    if input_file:
        os.remove(input_file)
    print("正在清理中间文件...")
    import shutil
    shutil.rmtree('sampleProject/gt_input')
    shutil.rmtree('sampleProject/gt_output')
    print("正在清理输出...")
    if output_srt:
        os.remove(output_srt)
    if output_lrc:
        os.remove(output_lrc)

with gr.Blocks() as demo:
    gr.Markdown("# 欢迎使用GalTransl for ASMR！")
    gr.Markdown("您可以使用本程序将日语音视频文件/字幕文件转换为中文字幕文件。")
    input_file = gr.File(label="1. 请选择音视频文件/SRT文件（或拖拽文件到窗口）")
    model_size = gr.Radio(
        label="2. 请选择语音识别模型大小:",
        choices=['small', 'medium', 'large-v3',],
        value='small'
    )
    from GalTransl import TRANSLATOR_SUPPORTED
    translator = gr.Radio(
        label="3. 请选择翻译器：",
        choices=list(TRANSLATOR_SUPPORTED.keys())[:6],
        value=list(TRANSLATOR_SUPPORTED.keys())[0]
    )
    gpt_token = gr.Textbox(label="4. 请输入GPT3.5/4 API Token", placeholder="留空为使用上次配置的Token")
    moonshot_token = gr.Textbox(label="5. 请输入Moonshot API Token", placeholder="留空为使用上次配置的Token，翻译器请选择GPT3.5")
    sakura_address = gr.Textbox(label="6. 请输入Sakura API地址", placeholder="留空为使用上次配置的地址")
    proxy_address = gr.Textbox(label="7. 请输入翻译引擎代理地址", placeholder="留空为不使用代理")

    run = gr.Button("8. 运行（状态详情请见命令行）")
    output_srt = gr.File(label="9. 字幕文件(SRT)")
    output_lrc = gr.File(label="10. 字幕文件(LRC)")
    clean = gr.Button("11.清空输入输出缓存（请在使用完成后点击）")

    run.click(worker, inputs=[input_file, model_size, translator, gpt_token, moonshot_token, sakura_address, proxy_address], outputs=[output_srt, output_lrc], queue=True)
    clean.click(cleaner, inputs=[input_file, output_srt, output_lrc])

demo.queue().launch(inbrowser=True, server_name='0.0.0.0')
