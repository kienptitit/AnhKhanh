import re

pattenrn = re.compile("^\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2}")

res = ""
with open('tz (1).txt', encoding="utf8") as f:
    for line in f:
        line = line.strip()
        if re.match(pattenrn, line) is not None:
            res += line + "\n"
with open('tmp.txt', 'w') as f:
    f.write(res)
