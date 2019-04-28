import re
import pandas as pd
from pandas import DataFrame


def openfile():
    name_ls = []
    first_score_ls = []
    second_score_ls = []
    file_ls = ["octane2_01.mhtml","octane2_01.mhtml"]  # add test files
    for file in file_ls:
        with open(file) as f:
            html = f.read()
            cont = html.replace("=\n", "")
        #print(cont)
        all_list = re.findall(r'>(\w*?\D*?)</a>[\s\W\w]*?>(\d+)</\w*?>[\s\W\w].*?>(.*?)</\w+?>', cont, re.S)
        # print(all_list, len(all_list))
        for all in all_list:
            name_ls.append(all[0])
            first_score_ls.append(all[1])
            second_score_ls.append(all[-1].split(',')[-1])
    print(name_ls, len(name_ls))
    print(first_score_ls, len(first_score_ls))
    print(second_score_ls, len(second_score_ls))

    return name_ls, first_score_ls, second_score_ls


def fix(count=3):  # count=test count
    all_ls = openfile()
    name = all_ls[0]
    first = all_ls[1]
    second = all_ls[2]
    df = DataFrame({"name": name[:17]})
    writer = pd.ExcelWriter("octane2.xls")
    header = DataFrame.__name__ = "octane2_benchmark"
    for i in range(0, count):
        elaspe = ["child"+str(i),"min"+str(i)]
        df[elaspe[0]] = first[i*17:(i+1)*17]
        df[elaspe[1]] = second[i*17:(i+1)*17]
    print(df)
    df.to_excel(writer, header=header, sheet_name='sheet1', na_rep='')
    writer.save()
    print("save done !!!")


def main():
    fix()


if __name__ == "__main__":
    main()
