import re


def srt2ass(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as srt_file:
        lines = srt_file.readlines()

    ass_lines = [
        "[Script Info]\n",
        "ScriptType: v4.00+\n",
        "Collisions: Normal\n",
        "PlayDepth: 0\n\n",
        "[V4+ Styles]\n",
        "Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, "
        "Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, "
        "MarginR, MarginV, Encoding\n",
        "Style: Default,Arial,20,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,1,1,2,10,10,10,1\n\n",
        "[Events]\n",
        "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
    ]

    dialogue_index = 1
    start_time, end_time, text = None, None, []

    for line in lines:
        #移除空行和换行符
        line = line.strip()

        #匹配时间戳
        time_match = re.match(r'(\d{2}:\d{2}:\d{2},\d{2}) --> (\d{2}:\d{2}:\d{2},\d{2})', line)
        if time_match:
            start_time = time_match.group(1).replace(',', '.')
            end_time = time_match.group(2).replace(',', '.')
            continue

        #匹配字幕编号
        if line.isdigit() and int(line) == dialogue_index:
            dialogue_index += 1
            continue

        if line:
            text.append(line)
        else:
            #遇到空行时，将当前文本行写入
            if start_time and end_time:
                text_content = "\\N".join(text)
                ass_line = f"Dialogue: 0,{start_time},{end_time},Default,,0,0,0,,{text_content}\n"
                ass_lines.append(ass_line)

            start_time, end_time, text = None, None, []

    with open(output_file, 'w', encoding='utf-8') as ass_file:
        ass_file.writelines(ass_lines)

