import requests
import json
import time
import re
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def LogIn():

    cookies_dict = {}  # cookies data dict
    DriverObj = webdriver.Chrome()
    DriverObj.delete_all_cookies()
    time.sleep(1)
    DriverObj.get("https://mp.weixin.qq.com/")
    DriverObj.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').clear()
    DriverObj.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[1]/div/span/input').send_keys('2207926014@qq.com')  # account
    time.sleep(1)
    DriverObj.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').clear()
    DriverObj.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[1]/div[2]/div/span/input').send_keys('weixin123')  # pwd
    time.sleep(2)
    DriverObj.find_element_by_xpath('//*[@id="header"]/div[2]/div/div/form/div[4]/a').click()
    time.sleep(15)
    print("Log in successfully !")
    DriverObj.get("https://mp.weixin.qq.com/")

    cookies_list = DriverObj.get_cookies()
    for cookies in cookies_list:
        cookies_dict[cookies['name']] = cookies['value']  # add all to one dict
    cookie_json = json.dumps(cookies_dict, ensure_ascii=False)  # dict become json
    with open("cookies.json", "w+") as f:
        f.write(cookie_json)

    print("cookies data write done !")


# TODO date collect because of IP of ban
def GetData(query):
    base_url = "https://mp.weixin.qq.com"
    with open("cookies.json", "r") as f:
        cookies = f.read()
        cookies = json.loads(cookies)
    r = requests.get(base_url, cookies=cookies)  # cookies is dict type
    url = r.url
    token_pattern = re.compile(r'token=(\d+)')
    token = token_pattern.findall(url)[0]  # fetch token field
    search_url = "https://mp.weixin.qq.com/cgi-bin/searchbiz?"
    params = {
        'action': 'search_biz',
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': 1,
        'random': random.random(),
        'query': query,
        'begin': 0,
        'count': 5
    }
    headers = {
        'Host': 'mp.weixin.qq.com',
        'Referer': 'https://mp.weixin.qq.com/cgi-bin/appmsg?t=media/appmsg_edit&action=edit&type=10&isMul=1&isNew=1&lang=zh_CN&token=212452637',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    search_r = requests.get(search_url, cookies=cookies, headers=headers, params=params)
    fakeid_dict = search_r.json()['list'][0]
    fakeid = fakeid_dict['fakeid']  # MzI4MTQ4NDAwMw==
    appmsg_url = "https://mp.weixin.qq.com/cgi-bin/appmsg?"
    begin = 0
    count = 1
    while not flags:
        try:
            print('The program is crawling page{}'.format(count))
            params_appmsg = {
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': 1,
                'random': random.random(),
                'action': 'list_ex',
                'begin': begin,          # click next page begin field add 5
                'count': 5,
                'query': '',
                'fakeid': fakeid,
                'type': 9
            }
            time.sleep(random.randint(2,5))
            r_appmasg = requests.get(appmsg_url, cookies=cookies, headers=headers, params=params_appmsg)
            print(r_appmasg.json())
            begin += 5
            count += 1
            # TODO

        except:
            pass
flags = False



def main():
    gzh = str(input('need one gzh:'))
    LogIn()
    GetData(gzh)


if __name__ == "__main__":
    main()


