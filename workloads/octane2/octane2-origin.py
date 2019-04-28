import re
import pandas as pd
from pandas import DataFrame


file_list = ["octane2_01.mhtml","octane2_02.mhtml"]


def Fetch(file):
    name_list = []
    score_list = []
    with open(file) as f:
        content = f.read()
        cont = content.replace("=\n", "")
    # print(cont)
    all_list = re.findall(r'>(\w+\.?\s?\w+)</a>[\d\D]*?>(\d+)<', cont)
    # print(len(all_list),"------")
    for i in all_list:
        name_list.append(i[0])
        score_list.append(i[1])
    return name_list, score_list


def Collect():
    score_ls = []
    name_ls = []
    for file in file_list:
        if file:
            a = Fetch(file)
            score = a[1]
            score_ls.append(a[1])
            name_ls.append(a[0])
    name_ls = name_ls[0]
    writer = pd.ExcelWriter("octane2-origin.xls")
    df = DataFrame({"scorename": name_ls})
    for i in range(len(file_list)):
        score = file_list[i].split('.')[0]
        df[score] = score_ls[i]
    print(df)

    df.to_excel(writer, sheet_name='sheet1')
    writer.save()
    print("----------------------good boy !!----------------------done !!")


def main():
    Collect()


if __name__ == "__main__":
    main()





