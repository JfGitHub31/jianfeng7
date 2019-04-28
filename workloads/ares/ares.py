import re
import pandas as pd
from pandas import DataFrame


file_list = ["ares_01.mhtml","ares_02.mhtml","ares_03.mhtml"]


def Fetch(file):
    name_list = []
    score_list = []
    with open(file) as f:
        content = f.read()
    cont = content.replace("=\n", "")
    all_list = re.findall(r'<span id=3D"(\w+)">[\d\D]*?>(\d+\.?\d*)', cont)
    target_list = all_list[1:]

    for i in target_list:
        name_list.append(i[0])
        score_list.append(i[1])

    return name_list, score_list


def Collect():
    name_list = []
    score_list = []
    for file in file_list:
        a = Fetch(file)
        score = a[1]
        score_list.append(a[1])
        name_list.append(a[0])
    name_list = name_list[0]
    writer = pd.ExcelWriter("ares.xls")
    df = DataFrame({"scorename": name_list})

    for i in range(len(file_list)):
        score = file_list[i].split('.')[0]
        df[score] = score_list[i]
    print(df)

    df.to_excel(writer, sheet_name='sheet1')
    writer.save()


def main():
    Collect()


if __name__ == "__main__":
    main()