import re


def ass2srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as ass_file:
        lines = ass_file.readlines()

    srt_lines = []
    dialogue_index = 1  # SRT开始序号为1

    for line in lines:
        # 只处理Dialogue开头的字幕行
        if line.startswith("Dialogue:"):
            # 用正则表达式提取
            match = re.match(r'Dialogue: \d+,(\d+:\d+:\d+\.\d+),(\d+:\d+:\d+\.\d+),[^,]+,[^,]*,\d+,\d+,\d+,[^,]*,(.*)',
                             line)
            if match:
                start_time = match.group(1)
                end_time = match.group(2)
                text = match.group(3).replace("\\N", "\n")  # 替换行内换行符
                # 去除字幕文本中{}里面的特效内容
                text = re.sub(r'\{.*?\}', '', text)

                #毫秒格式转换
                start_time = start_time.replace('.', ',')
                end_time = end_time.replace('.', ',')

                #0补齐
                if start_time.count(':') == 2 and len(start_time.split(':')[0]) == 1:
                    start_time = '0' + start_time
                if end_time.count(':') == 2 and len(end_time.split(':')[0]) == 1:
                    end_time = '0' + end_time

                srt_lines.append(f"{dialogue_index}\n{start_time} --> {end_time}\n{text}\n\n")
                dialogue_index += 1

    with open(output_file, 'w', encoding='utf-8') as srt_file:
        srt_file.writelines(srt_lines)

