# convert srt file to prompt file

import json, argparse
from datetime import timedelta

def make_prompt(input_file, output_file):
    # read srt file
    with open(input_file, encoding='utf-8') as f:
        lines = f.readlines()
    # parse srt file
    data = []
    for i in range(0, len(lines)):
        if not lines[i].strip().isdigit():
            continue
        
        start, end = lines[i+1].strip().split(" --> ")

        # hh:mm:ss,ms to seconds
        start = sum(x * int(t) for x, t in zip([3600, 60, 1, 0.001], start.replace(",",":").split(":")))

        end = sum(x * int(t) for x, t in zip([3600, 60, 1, 0.001], end.replace(",",":").split(":")))

        message = lines[i+2].strip()
        data.append({"start": start, "end": end, "message": message})
    # write prompt file
    with open(output_file, 'w', encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--input_file", type=str, required=True)
    parser.add_argument("-o","--output_file", type=str, required=True)
    args = parser.parse_args()
    make_prompt(args.input_file, args.output_file)