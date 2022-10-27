from collections import defaultdict
from Get_MaSV import MaSV
import re
import os
import json

Sv = defaultdict(list)
Re = re.compile("B\\d{2}DCDT\\d{3}.+")
suf_file = ['.docx']
test = []
with open('tmp.txt', encoding="utf8", errors="ignore") as f:
    for line in f:
        line = line.strip()
        line = re.findall(Re, line)
        if len(line) > 0:
            line = line[0]
            ma_sv = re.findall(MaSV, line)[0]
            idx = line.rfind('\\')
            name_file = line[idx + 1:]
            name_file.strip()
            if '.' in name_file:
                Sv[ma_sv].append(os.path.splitext(name_file))

SV1 = defaultdict(dict)
for key, item in Sv.items():
    wat_Count = 0
    txt_count = 0
    docx_count = 0
    for i in item:
        if i[-1] == '.wav':
            wat_Count += 1
        if i[-1] == '.txt':
            txt_count += 1
        if i[-1] == '.docx':
            docx_count += 1
    SV1[key]["nWavFile"] = wat_Count
    SV1[key]["nTxtFile"] = txt_count
    SV1[key]["nDocxFile"] = docx_count

with open('Data_file.json', 'w') as f:
    json.dump(SV1, f)

for key, value in Sv.items():
    if not os.path.exists(key):
        os.mkdir(key)
    names = [''.join(tmp) for tmp in value if tmp[-1] == '.txt']
    Names = [os.path.join(key, name) for name in names]
    cnt = 1
    for name in Names:
        with open(name, 'w') as f:
            f.write(str(cnt))
            cnt += 1
