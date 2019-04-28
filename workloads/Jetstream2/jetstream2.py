import re
import pandas as pd
from pandas import DataFrame

file_list = ["JetStream2_00.mhtml","JetStream2_01.mhtml"]


def fun1(file):
    name_ls = []
    score_ls = []
    with open(file) as f:
        pass
        content = f.read()

    cont = content.replace("=\n", "")

    cont_ls = re.findall(r'<h3[\d\D]*?><[\d\D]*?>(.*?)</a></h3>[\d\D]*?<h4[\d\D]*?>(.*?)</h4>', cont, re.S)
    print(len(cont_ls))

    for i in cont_ls:
        name_ls.append(i[0])
        score_ls.append(i[1])

    return name_ls, score_ls


def fun2():
    name_ls = []
    score_ls = []

    for file in file_list:
        if file:
            a = fun1(file)
            name_ls.append(a[0])
            score_ls.append(a[1])
            name = name_ls[0]
    name_ls = name_ls[0]

    writer = pd.ExcelWriter("Jetstream2.xls")
    df = DataFrame({"name": name_ls})

    for i in range(len(file_list)):
        score = file_list[i].split('.')[0]
        df[score] = score_ls[i]
    print(df)

    df.to_excel(writer, sheet_name='sheet1')
    writer.save()


def main():
    fun2()


if __name__ == "__main__":
    main()








# [('3d-cube-SP', '46.735'), ('3d-raytrace-SP', '160.125'), ('acorn-wtb', '24.458')]