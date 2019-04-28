import re
import requests
import random
import time
import threading
import queue
from lxml import etree
from fake_useragent import UserAgent


UA = UserAgent(use_cache_server=False)
headers = {"User-Agent": UA.random}


class ThreadUrl(threading.Thread):
    def __init__(self, new_name, new_queue_url, new_queue_info):
        super(ThreadUrl, self).__init__()
        self.name = new_queue_url
        self.queue_url = new_queue_url
        self.queue_info = new_queue_info

    def run(self, city="欧洲"):  # city can be modified
        while True:
            try:
                time.sleep(random.random())
                page = self.queue_url.get(block=False)
                url = "http://s.tuniu.com/search_complex/whole-sh-0-" + city + "/" + str(page)
                r = requests.get(url, headers=headers)
                r.encoding = "utf-8"
                html = r.text
                cont = etree.HTML(html)
                url_ls = cont.xpath("//div[@class='theinfo']/a[@class='clearfix']/@href")
                for item in url_ls:
                    url = "http:" + item
                    print(url)
                    r = requests.get(url, headers=headers)
                    r.encoding = "utf-8"
                    html = r.text
                    # print(html)
                    self.queue_info.put(html)
            except Exception as e:
                print(e)
                break


class TheadData(threading.Thread):
    def __init__(self, new_name, new_queue_info):
        super(TheadData, self).__init__()
        self.name = new_name
        self.queue_info = new_queue_info

    def run(self):
        while True:
            try:
                time.sleep(random.random())
                html = self.queue_info.get(block=False)
                title_ls = re.findall(r'<h1 class="resource-title"><strong>(.*?)</strong>', html, re.S)
                p_ls = re.findall(r'<meta content="(.*?)" name="description" />', html, re.S)
                price_ls = re.findall(r'\d+', ''.join(p_ls), re.S)
                count_ls = re.findall(r'<div class="resource-people-item">.*?<a class="resource-people-number" href="javascript:;">(.*?)</a></div>', html, re.S)
                comment_ls = re.findall(r'<div class="resource-people-item">.*?<a class="resource-people-number" href="#comment" mm=.*?>(.*?)</a></div>', html, re.S)
                st_ls = re.findall(r'<a class="resource-statisfaction-number" href="#comment" mm=.*?>(.*?)<span class="resource-statisfaction-percent">%</span></a>', html, re.S)

                title = ''.join(title_ls)
                price = ''.join(price_ls)
                count = ''.join(count_ls)
                comment = ''.join(comment_ls)
                st_percent = ''.join(st_ls)
                print([title, price, count, comment, st_percent])
            except Exception as e:
                print(e)
                break


def main(page=45):  # page can be modified

    queue_url = queue.Queue()
    for i in range(1, page):
        queue_url.put(i)

    queue_info = queue.Queue()
    T_url_ls = []
    ThreadUrlName = ["number1", "number2", "number3"]
    for url_name in ThreadUrlName:
        T_url = ThreadUrl(url_name, queue_url, queue_info)
        T_url.start()
        T_url_ls.append(T_url)
    for T_url in T_url_ls:
        T_url.join()

    T_data_ls = []
    ThreadDataName = ["number1", "number2", "number3"]
    for data_name in ThreadDataName:
        T_data = TheadData(data_name, queue_info)
        T_data.start()
        T_data_ls.append(T_data)
    for T_data in T_data_ls:
        T_data.join()


if __name__ == "__main__":
    main()






















#headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}