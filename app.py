# follow main.py to create a web-based demo
import sys, os
sys.path.append(os.path.dirname(__file__))
import gradio as gr

TRANSLATOR_SUPPORTED = [
    "sakura-009",
    "sakura-010",
    "index",
    "gpt35-0613",
    "gpt35-1106",
    "gpt4-turbo",
    "moonshot-v1-8k",
    "glm-4",
    "glm-4-flash",
    "qwen2-7b-instruct",
    "qwen2-57b-a14b-instruct",
    "qwen2-72b-instruct",
    "abab6.5-chat",
    "abab6.5s-chat",
]

def worker(input_file, model_size, translator, gpt_token, sakura_address, proxy_address):
    if input_file.endswith('.srt'):
        from srt2prompt import make_prompt
        print("正在进行字幕转换...")
        import os
        os.makedirs('sampleProject/gt_input', exist_ok=True)
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
        if 'gpt' in translator and gpt_token:
            if 'GPT35' in line:
                lines[idx+2] = f"      - token: {gpt_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://api.openai.com\n"
                lines[idx+7] = f'    rewriteModelName: ""\n'
            if 'GPT4' in line:
                lines[idx+2] = f"      - token: {gpt_token}\n"
        if 'moonshot' in translator and gpt_token:
            if 'GPT35' in line:
                lines[idx+4] = f"      - token: {gpt_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://api.moonshot.cn\n"
                lines[idx+7] = f'    rewriteModelName: "moonshot-v1-8k"\n'
        if 'qwen' in translator and gpt_token:
            if 'GPT35' in line:
                lines[idx+4] = f"      - token: {gpt_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://dashscope.aliyuncs.com/compatible-mode\n"
                lines[idx+7] = f'    rewriteModelName: "{translator}"\n'
        if 'glm' in translator and gpt_token:
            if 'GPT35' in line:
                lines[idx+4] = f"      - token: {gpt_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://open.bigmodel.cn/api/paas\n"
                lines[idx+7] = f'    rewriteModelName: "{translator}"\n'
        if 'abab' in translator and gpt_token:
            if 'GPT35' in line:
                lines[idx+4] = f"      - token: {gpt_token}\n"
                lines[idx+6] = f"    defaultEndpoint: https://api.minimax.chat\n"
                lines[idx+7] = f'    rewriteModelName: "{translator}"\n'
        if ('sakura' in translator or 'index' in translator) and sakura_address:
            if 'Sakura' in line:
                lines[idx+1] = f"    endpoint: {sakura_address}\n"
        if proxy_address:
            if 'proxy' in line:
                lines[idx+1] = f"  enableProxy: true\n"
                lines[idx+3] = f"    - address: {proxy_address}\n"
        else:
            if 'proxy' in line:
                lines[idx+1] = f"  enableProxy: false\n"

    if 'moonshot' in translator or 'qwen' in translator or 'glm' in translator or 'abab' in translator:
        translator = 'gpt35-0613'
    
    if 'index' in translator:
        translator = 'sakura-009'

    with open('sampleProject/config.yaml', 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print("正在进行翻译...")
    from GalTransl.__main__ import worker
    worker('sampleProject', 'config.yaml', translator, show_banner=False)

    print("正在生成字幕文件...")
    from prompt2srt import make_srt, make_lrc
    make_srt(output_file_path.replace('gt_input','gt_output'), input_file+'.srt')
    make_lrc(output_file_path.replace('gt_input','gt_output'), input_file+'.lrc')
    make_srt(output_file_path, input_file+'.jp.srt')
    print("字幕文件生成完成！")
    print("输入输出缓存地址为：", os.path.dirname(input_file))
    return input_file+'.srt', input_file+'.lrc', input_file+'.jp.srt'

def cleaner(input_file, output_srt, output_lrc, output_jp_srt):
    print("正在清理输入...")
    if input_file:
        os.remove(input_file)
    print("正在清理中间文件...")
    import shutil
    shutil.rmtree('sampleProject/gt_input')
    shutil.rmtree('sampleProject/gt_output')
    shutil.rmtree('sampleProject/transl_cache')
    print("正在清理输出...")
    if output_srt:
        os.remove(output_srt)
    if output_lrc:
        os.remove(output_lrc)
    if output_jp_srt:
        os.remove(output_jp_srt)

with gr.Blocks() as demo:
    gr.Markdown("# 欢迎使用GalTransl for ASMR！")
    gr.Markdown("您可以使用本程序将日语音视频文件/字幕文件转换为中文字幕文件。")
    input_file = gr.File(label="1. 请选择音视频文件/SRT文件（或拖拽文件到窗口）")
    model_size = gr.Radio(
        label="2. 请选择语音识别模型大小:",
        choices=['small', 'medium', 'large-v3',],
        value='small'
    )
    translator = gr.Radio(
        label="3. 请选择翻译器：",
        choices=TRANSLATOR_SUPPORTED,
        value=TRANSLATOR_SUPPORTED[0]
    )
    gpt_token = gr.Textbox(label="4. 请输入 API Token (GPT, Moonshot, Qwen, GLM, MiniMax/abab)", placeholder="留空为使用上次配置的Token")
    sakura_address = gr.Textbox(label="6. 请输入 API 地址 (Sakura, Index)", placeholder="留空为使用上次配置的地址")
    proxy_address = gr.Textbox(label="7. 请输入翻译引擎代理地址", placeholder="留空为不使用代理")

    run = gr.Button("8. 运行（状态详情请见命令行）")
    output_srt = gr.File(label="9. 字幕文件(SRT)", interactive=False)
    output_lrc = gr.File(label="10. 字幕文件(LRC)", interactive=False)
    output_jp_srt = gr.File(label="11. 日语字幕文件(SRT)", interactive=False)
    clean = gr.Button("12.清空输入输出缓存（请在使用完成后点击）")

    run.click(worker, inputs=[input_file, model_size, translator, gpt_token, sakura_address, proxy_address], outputs=[output_srt, output_lrc, output_jp_srt], queue=True)
    clean.click(cleaner, inputs=[input_file, output_srt, output_lrc, output_jp_srt])

demo.queue().launch(inbrowser=True, server_name='0.0.0.0')
