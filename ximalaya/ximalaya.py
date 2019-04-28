import os
import json
import requests
import time
import random
from lxml import etree


def GetHtml(base_url):

    time.sleep(random.random())
    # proxy = {'http': '33.33.33.10:8118'}
    r = requests.get(base_url, headers=headers,timeout=30)
    r.encoding = 'utf-8'
    content = r.text
    html = etree.HTML(content)
    return html


def GetUrl(type_xpath):
    next_url_list = []
    html = GetHtml(base_url)
    url_list = html.xpath(type_xpath)
    for item_url in url_list:
        next_url = ["https://www.ximalaya.com" + item_url + "p{}".format(i) for i in range(2,29)]
        next_url_list.extend(next_url)
    return next_url_list


def GetChildUrl():
    ChildList = []
    GetUrl_list = GetUrl(type_xpath)
    for GetUrl_item in GetUrl_list:
        time.sleep(random.random())
        html = GetHtml(GetUrl_item)
        child_url_list = html.xpath(child_xpath)
        ChildList += child_url_list
    child_set = set(ChildList)
    # print(child_set)
    return child_set


def GetTargetUrl(radio_xpath):
    radio_list = []
    child_set = GetChildUrl()
    for item_set in child_set:
        target_url = "https://www.ximalaya.com" + item_set
        radio_ls = GetHtml(target_url).xpath(radio_xpath)
        radio_list += radio_ls
    return radio_list


def Final():
    folder = r'D:\ximalaya'
    final_list = GetTargetUrl(radio_xpath)
    count = 1
    for final_item in final_list:
        final_url = api_url + final_item.split('/')[3]
        # print(final_url)
        try:
            r = requests.get(final_url, headers=headers, timeout=30)
            api_dict = json.loads(r.text)['data']['tracksForAudioPlay'][0]

            name = api_dict['trackName']
            # print(api_dict['src'])
            f = requests.get(api_dict['src'])
            print('正在下载第{}个音频--->名字是{}'.format(count, name))
            if os.path.exists(folder):
                with open(r"D:\ximalaya\{}.mp4".format(name), "wb") as code:
                    code.write(f.content)
            elif not os.path.exists(folder):
                os.mkdir(folder)
                with open(r"D:\ximalaya\{}.mp4".format(name), "wb") as code:
                    code.write(f.content)
        except Exception as e:
            print(e)
        count += 1


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    base_url = "https://www.ximalaya.com/category/#%E7%94%9F%E6%B4%BB"
    type_xpath = "//div[@class='hW1c category_plate'][1]/div[@class='hW1c body']/section[@class='hW1c subject_wrapper'][3]/div[@class='hW1c list']/a[@class='hW1c item separator']/@href"
    child_xpath = "//div[@class='HxMH album-wrapper ']/a[@class='HxMH album-title lg']/@href"
    radio_xpath = "//div[@class='dOi2 text']/a//@href"
    api_url = "https://www.ximalaya.com/revision/play/tracks?trackIds="
    Final()
