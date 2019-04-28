import random
import time
import requests
from lxml import etree


def GetPro(page):
    proxy_dt = {}
    pro_ls = []
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        }
    url_list = ["http://www.xicidaili.com/nn/{}".format(i) for i in range(1,page+1)]
    for item in url_list:
        try:
            time.sleep(random.random())
            r = requests.get(item, headers=headers)
            r.encoding = "UTF-8"
            cont = r.text
            html = etree.HTML(cont)
            ip_list = html.xpath('//*[@id="ip_list"]/tr/td[2]/text()')
            type_list = html.xpath('//*[@id="ip_list"]/tr/td[6]/text()')

            for index, ite in enumerate(ip_list):
                proxy_dt[type_list[index]] = ite
                data = {type_list[index]:ip_list[index]}
                pro_ls.append(data)
        except Exception as e:
            print(e)
    return random.choice(pro_ls)

