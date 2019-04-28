import requests
import re
import pandas as pd
from pandas import DataFrame
from fake_useragent import UserAgent
from bs4 import BeautifulSoup


def GetCookie():
    url = "https://passport.bilibili.com/login"
    UA = UserAgent(use_cache_server=False)
    headers = {"User-Agent": UA.random}
    data = {"user": "18238641800", "pwd": "bilibili123"}
    r = requests.post(url, data=data, headers=headers)
    cookies = r.cookies.get_dict()

    def GetData(query, page):
        href_list = []
        title_list = []
        manuscript_list = []
        fans_list = []
        for number in range(2, page):
            url_api = "https://search.bilibili.com/upuser?keyword=" + query + "&page=" + str(number)
            r = requests.get(url_api, headers=headers, cookies=cookies)
            r.encoding = "UTF-8"
            html = r.text
            soup = BeautifulSoup(html, "html.parser")
            a_ls = soup.find_all("a", attrs={"href", "title", "target", "class"})
            div_ls = re.findall(r'<div class="up-info clearfix">(.*?)</div>', html, re.S)
            for a in a_ls:
                href = a.attrs['href']
                title = a.attrs['title']
                hrefs = href.split("?")[0].split("/")[-1]
                href_list.append(hrefs)  # href info of number
                title_list.append(title)  # title
            for items in div_ls:
                items_list = re.findall(r'<span>(.*?)</span>', items)
                ms = re.sub("\D", "", items_list[0])
                manuscript_list.append(int(ms))  # manuscript
                fan = re.sub("\D", "", items_list[1])
                fans_list.append(int(fan))  # fans

        def Collect():
            data = {
                    "users": title_list,
                    "manuscript": manuscript_list,
                    "fans": fans_list,
                    "url_info": href_list
                   }
            dataframe = DataFrame(data)
            header = DataFrame.__name__ = "bilibili upusers data"
            print(header)
            print(dataframe)
            writer_obj = pd.ExcelWriter("bilibili.xls")  # save xls format
            dataframe.to_excel(
                                writer_obj,
                                header=header,
                                sheet_name='sheet1',
                                na_rep='',
                                index=True
                              )
            writer_obj.save()
            print("data saved to excel !")
        return Collect

    return GetData


if __name__ == "__main__":
    fun = GetCookie()
    show = fun("科技", 20)  # input query and pages
    show()





