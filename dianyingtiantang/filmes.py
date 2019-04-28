import requests
import urllib.request
import xlwt
from lxml import etree


all_info_list = []
def GetHtml(base_url):
    r = requests.get(base_url, headers=headers)
    r.encoding = 'GB2312'
    html = r.text
    content = etree.HTML(html)
    return content


def GetPageUrl(base_url, type_url_xpath):
    info_url_list = []
    type_url_list = GetHtml(base_url).xpath(type_url_xpath)

    html_list = ["list_23_{}.html".format(i) for i in range(1,180)]
    for item in html_list:
        info_url = type_url_list[0][:-10] + item
        info_url_list.append(info_url)
    return info_url_list


def GetFilmesUrls(filmes_url_xpath):
    filmes_all_url_list = []
    for date_url in GetPageUrl(base_url, type_url_xpath):
        filmes_url_list = GetHtml(date_url).xpath(filmes_url_xpath)
        filmes_all_url_list.extend(filmes_url_list)
    return filmes_all_url_list  # 电影详情url


def GetFilmesInfo(name_xpath, type_xpath, date_xpath, score_xpath, time_xpath):
    count = 0
    for url in GetFilmesUrls(filmes_url_xpath):
        filmes_url = "http://www.ygdy8.net" + url
        count += 1
        print('正在爬取第%d部影片信息'%count)
        # print('当前爬取进度{:.2f}%'.format(count*100/len(GetFilmesUrls(filmes_url_xpath))))
        try:
            name = GetHtml(filmes_url).xpath(name_xpath)[0]
            type = GetHtml(filmes_url).xpath(type_xpath)[0]
            date = GetHtml(filmes_url).xpath(date_xpath)[0]
            score = GetHtml(filmes_url).xpath(score_xpath)[0]
            time = GetHtml(filmes_url).xpath(time_xpath)[0]
            info_list = [name, type, date, score, time]
            all_info_list.append(info_list)
        except:
            print('该处异常已跳过')
    return all_info_list


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'}
    base_url = 'http://www.dytt8.net/'
    type_url_xpath = "//div[@id='menu']/div[@class='contain']/ul/li[1]/a//@href"
    filmes_url_xpath = "//tr[2]/td[2]/b/a[@class='ulink']//@href"
    name_xpath = '//*[@id="Zoom"]//text()[3]'
    type_xpath = '//*[@id="Zoom"]//text()[7]'
    date_xpath = '//*[@id="Zoom"]//text()[10]'
    score_xpath = '//*[@id="Zoom"]//text()[12]'
    time_xpath = '//*[@id="Zoom"]//text()[16]'
    # GetPageUrl(base_url, type_url_xpath)
    # GetFilmesUrls(filmes_url_xpath)
    GetFilmesInfo(name_xpath, type_xpath, date_xpath, score_xpath, time_xpath)

    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('最新电影大全')
    head_info = ['影片名称', '影片类型', '豆瓣评分', '影片时长']
    for head in range(len(head_info)):
        sheet.write(0,head,head_info[head])
    i = 1
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('demo.xls')


