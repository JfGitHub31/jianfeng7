#!/usr/bin/env python
import requests
import threading
import queue
import time
import re
import os
import json
import random
from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver


info_list = []
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
           "authority": "search.jd.com",
           "referer": "https://search.jd.com/Search?keyword=%E5%B8%BD%E5%AD%90&enc=utf-8"
           }


class CrawlThread(threading.Thread):

    def __init__(self, new_thread_url_name, new_queue_url, new_queue_info, new_goods_name):
        super(CrawlThread, self).__init__()
        self.thread_url_name = new_thread_url_name
        self.queue_url = new_queue_url
        self.queue_info = new_queue_info
        self.goods_name = new_goods_name
        self.headers = headers

    def run(self):
        while 1:
            time.sleep(random.random())
            try:
                print("%s is launching" % self.thread_url_name)
                ls = self.queue_url.get(block=False)
                url = "https://search.jd.com/Search?keyword=" + self.goods_name + "&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=" + str(ls[0]) + "&s=" + str(ls[1]) + "&click=0"
                r = requests.get(url, headers=self.headers)
                r.encoding = 'utf-8'
                html = r.text
                self.queue_info.put(html)
            except:
                print("%s is done !" % self.thread_url_name)
                break


class ParseThread(threading.Thread):

    def __init__(self, new_parse_info_name, new_queue_info):
        super(ParseThread, self).__init__()
        self.parse_info_name = new_parse_info_name
        self.queue_info = new_queue_info
        self.headers = headers

    def run(self):
        while True:
            time.sleep(random.random())
            try:
                html = self.queue_info.get(False)
                self.parse(html)
            except:
                break

    def parse(self, html):
        hls = []
        try:
            soup = BeautifulSoup(html, "html.parser")
            a_ls = soup.find_all('a')
            for a_item in a_ls:
                href = a_item.attrs['href']
                href_ls = re.findall(r'^/+\bitem\b.+\bhtml\b$', href)
                if len(href_ls):
                    hls.append(href_ls[0])
            sls = set(hls)
            for sls_item in sls:
                url_info = "https:" + sls_item
                info_list.append(url_info)
            return info_list
        except Exception as e:
            print(e)


def main():
    queue_info = queue.Queue()
    queue_url = queue.Queue()
    page = 1
    s = 1
    for i in range(1, 3):
        queue_url.put([page, s])
        page += 2
        s += 53
    crawl_url_num = []
    goods_name = input("goods_type is needed: ")
    crawl_url_thread_list = ["crawl_url_thread_01", "crawl_url_thread_02", "crawl_url_thread_03"]
    for crawl_url_thread in crawl_url_thread_list:
        crawl_thread = CrawlThread(crawl_url_thread, queue_url, queue_info, goods_name)
        crawl_thread.start()
        crawl_url_num.append(crawl_thread)
    for crawl_thread in crawl_url_num:
        crawl_thread.join()
    parse_info_num = []
    parse_info_thread_list = ["parse_info_01", "parse_info_02", "parse_info_03"]
    for parse_info_name in parse_info_thread_list:
        parse_info_thread = ParseThread(parse_info_name, queue_info)
        parse_info_thread.start()
        parse_info_num.append(parse_info_thread)
    for parse_info_thread in parse_info_num:
        parse_info_thread.join()

    def final():  # TODO save data
        print(info_list,len(info_list))
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver_obj = webdriver.Chrome(chrome_options=options)
        for item in info_list:
            driver_obj.get(item)
            r = driver_obj.page_source
            html = etree.HTML(r)
            title_list = html.xpath("/html/body/div[8]/div/div[2]/div[1]/text()")
            title = ''.join(title_list).replace(" ", "").replace("\n", "").replace("?", "")
            price_list = html.xpath("/html/body/div[8]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]/text()")
            price = ''.join(price_list)
            jpg_list = html.xpath('//*[@id="spec-list"]/ul/li/img/@src')
            item = {title: price}

            print(title, price)
    return final


if __name__ == "__main__":
    final_func = main()
    final_func()