import json, os, time,re


def write_out_to_log(payload,region):
    unix = str(int(time.time()))
    region = re.sub(' ', '-', region)
    file_name = '/home/rodrigocoelho/dotfiles/data/' + region + '-' + unix + '.txt'
    with open(file_name, 'w') as f:
        json.dump(payload, f, ensure_ascii=False)

