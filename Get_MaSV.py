import re

MaSV = re.compile("^B\\d{2}DCDT\\d{3}")
masv = []
with open('tmp.txt', 'r') as f:
    for line in f:
        line = line.strip().split()[-1].strip()
        match = re.findall(MaSV, line)
        if len(match) > 0:
            masv.append(match[0])

DSSV = set(masv)
