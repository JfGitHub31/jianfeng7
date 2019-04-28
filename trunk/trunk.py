import xlwt
from lxml import etree


all_score_list = []


def OpenFile(file):
    with open(file) as f:
        html = f.read()
        content = etree.HTML(html)
    return content


def FetchData():
    score_01 = OpenFile(file).xpath('//*/table[2]/tr[2]/td[1]/text()')
    print(score_01[0])
    score_02 = OpenFile(file).xpath('//*/table[2]/tr[3]/td[1]/text()')
    print(score_02[0])
    score_03 = OpenFile(file).xpath('//*/table[2]/tr[4]/td[1]/text()')
    print(score_03[0].replace('=\n', ""))
    score_04 = OpenFile(file).xpath('//*/table[2]/tr[5]/td[1]/text()')
    print(score_04[0])
    score_05 = OpenFile(file).xpath('//*/table[2]/tr[6]/td[1]/text()')
    print(score_05[0])
    score_06 = OpenFile(file).xpath('//*/table[2]/tr[7]/td[1]/text()')
    print(score_06[0])
    score_07 = OpenFile(file).xpath('//*/table[2]/tr[8]/td[1]/text()')
    print(score_07[0])
    score_08 = OpenFile(file).xpath('//*/table[2]/tr[9]/td[1]/text()')
    print(score_08[0])
    score_09 = OpenFile(file).xpath('//*/table[2]/tr[10]/td[1]/text()')
    print(score_09[0])
    score_10 = OpenFile(file).xpath('//*/table[2]/tr[11]/td[1]/text()')
    print(score_10[0])
    score_11 = OpenFile(file).xpath('//*/table[2]/tr[12]/td[1]/text()')
    print(score_11[0])
    score_12 = OpenFile(file).xpath('//*/table[2]/tr[13]/td[1]/text()')
    print(score_12[0])
    score_13 = OpenFile(file).xpath('//*/table[2]/tr[14]/td[1]/text()')
    print(score_13[0])
    score_14 = OpenFile(file).xpath('//*/table[2]/tr[15]/td[1]/text()')
    print(score_14[0])
    score_15 = OpenFile(file).xpath('//*/table[2]/tr[16]/td[1]/text()')
    print(score_15[0])
    score_16 = OpenFile(file).xpath('//*/table[2]/tr[17]/td[1]/text()')
    print(score_16[0])
    score_list = [score_01[0], score_02[0], score_03[0].replace('=\n', ""), score_04[0], score_05[0], score_06[0],
                      score_07[0], score_08[0], score_09[0], score_10[0], score_11[0], score_12[0], score_13[0],
                      score_14[0], score_15[0], score_16[0]]
    all_score_list.append(score_list)
    print(all_score_list, len(all_score_list))
    return all_score_list


def SaveData():
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet("trunk_fetch_score")
    head_info_list = ["VanillaJS-TodoMVC", "Vanilla-ES2015-TodoMVC", "Vanilla-ES2015-Babel-Webpack-TodoMVC", "React-TodoMVC",
                      "React-Redux-TodoMVC", "EmberJS-TodoMVC", "EmberJS-Debug-TodoMVC", "BackboneJS-TodoMVC",
                      "AngularJS-TodoMVC", "Angular2-TypeScript-TodoMVC", "VueJS-TodoMVC", "jQuery-TodoMVC",
                      "Preact-TodoMVC", "Inferno-TodoMVC", "Elm-TodoMVC", "Flight-TodoMVC"]

    i = 0
    j = 1

    for head in range(len(head_info_list)):
        sheet.write(i, 0, head_info_list[head])
        i += 1

    for child_list in all_score_list:

        n = 0
        for item in child_list:
             sheet.write(n, j, item)
             n += 1

        j += 1
    book.save("trunk_score.xls")


if __name__ == "__main__":
    all_file_list = ["eletro_01.mhtml", "eletro_02.mhtml", "eletro_03.mhtml",
                     "elm_01.mhtml", "elm_02.mhtml", "elm_03.mhtml",
                     "glk_01.html", "glk_02.html", "glk_03.html"]

    for file in all_file_list:
         if file == all_file_list[0]:
             FetchData()
         elif file == all_file_list[1]:
             FetchData()
         elif file == all_file_list[2]:
             FetchData()
         elif file == all_file_list[3]:
             FetchData()
         elif file == all_file_list[4]:
             FetchData()
         elif file == all_file_list[5]:
             FetchData()
         elif file == all_file_list[6]:
             FetchData()
         elif file == all_file_list[7]:
             FetchData()
         elif file == all_file_list[8]:
             FetchData()
    SaveData()
    print('数据收集完成')