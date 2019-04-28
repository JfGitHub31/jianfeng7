import requests
import PXY
import demjson
import re
from imp import reload
from jsonpath import jsonpath


reload(PXY)
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
            }


def GetUrl(query, page):  # query is you look for keyword  page look for numbers of pages in multiples 20
    info_url_ls = []
    proxy = PXY.GetPro(2)  # proxy IP pages in multiples of 1
    base_url = "https://www.toutiao.com/search_content/?"
    for i in range(0, page, 20):

        data = {
            "offset": i,
            "format": "json",
            "keyword": query,
            "autoload": "true",
            "count": "20",
            "cur_tab": "1",
            "from": "search_tab"
        }
        try:
            r = requests.get(base_url, headers=headers, params=data, proxies=proxy)
            print(r.status_code)
            r.encoding = "gbk"
            cont = r.json()
            # print("----------------------->",type(cont))
            article_url_ls = jsonpath(cont, "$..article_url")
            info_url_ls.extend(article_url_ls)
        except Exception as e:
            print(e)

    def parse():
        for info_url in info_url_ls:
            r = requests.get(info_url, headers=headers)
            r.encoding = 'utf-8'
            cont = r.text
            cont_data = re.findall(r'<script>(.*?)</script>', cont, re.S)

            for item in cont_data:
                if 'BASE_DATA' in item:
                    item = item[:-1].strip("var BASE_DATA = ").replace(".replace(/<br \/>/ig, '')", "")
                    py_obj = demjson.decode(item)
                    title = jsonpath(py_obj, "$..title")
                    tit = title[0]
                    content = jsonpath(py_obj, "$..content")
                    cot = re.findall(r'[\u4e00-\u9fa5]+', content[0], re.S)
                    cnt = ''.join(cot)
                    print({tit: cnt})
    return parse


if __name__ == "__main__":

    fun = GetUrl("旅游", 80)
    fun()