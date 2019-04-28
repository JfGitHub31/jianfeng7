import re
import pandas as pd
from pandas import DataFrame


file_list = [
             "eve_01.mhtml", "eve_02.mhtml", "eve_03.mhtml",
             "glk_01.mhtml", "glk_02.mhtml", "glk_03.mhtml",
             "whl_01.mhtml","whl_02.mhtml","whl_03.mhtml",
             ]
#file_list = ["base_01.mhtml","base_02.mhtml","base_03.mhtml"]


def transform(file):
    name_ls = []
    score_ls = []
    with open(file) as f:
        content = f.read()
    a = re.findall(r'<table class=3D"results-table">[\d\D]*?</table>', content)
    for i in a:
        if "Subcase" in i:
            i = i.replace("=\n", "")
            g = re.findall(r'<th>(.*?)</th>[\d\D]*?<td>(.*?)</td>[\d\D]*?<td>.*?</td>', i)
            item_list = g[1:]
            for item in item_list:
                name_ls.append(item[0])
                score_ls.append(item[1])

    return name_ls, score_ls


def Collect():
    score_ls = []
    name_ls = []
    for file in file_list:
        if file:
            a = transform(file)
            score = a[1]
            score_ls.append(a[1])
            name_ls.append(a[0])
    name_ls = name_ls[0]
    writer = pd.ExcelWriter("speedometer2.xls")
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


