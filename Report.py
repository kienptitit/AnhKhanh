import json

with open("Data_file.json", 'r') as f:
    data = json.load(f)
    res = ""
    for key, value in data.items():
        res += "=" * 30 + "\n"
        res += key + "\n"
        res += " ---> "
        res += str(value["nWavFile"]) + " wav file(s)" + "\n"
        res += " ---> "
        res += str(value["nTxtFile"]) + " text file(s)" + "\n"
        res += " ---> "
        res += str(value["nDocxFile"]) + " docx file(s)" + "\n"
    with open("Report.txt", "w") as f:
        f.write(res)
