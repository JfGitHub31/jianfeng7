import scrapy
from douban250.items import Douban250Item
from scrapy.http import Request
from fake_useragent import UserAgent


class Db250(scrapy.Spider):
    name = "douban250"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "referer": "https://movie.douban.com/top250"
    }
    cookies = {"form_email": "18238641800", "form_password": "douban123", "redir": "https://movie.douban.com/", "login": "登录"}

    def start_requests(self):
        url = ["https://movie.douban.com/top250?start={}&filter=".format(i) for i in range(0, 225, 25)]
        for i in url:
            yield Request(i, headers=self.headers, meta={'dont_redirect': True}, cookies=self.cookies, encoding='utf-8')

    def parse(self, response):
        item = Douban250Item()
        url_info = response.xpath('//div[@class="hd"]/a/@href').extract()
        for info in url_info:
            yield Request(info, headers=self.headers, callback=self.detail, meta={"A": item}, encoding='utf-8')

    def detail(self, response):
        item = response.meta["A"]
        item['title'] = response.xpath("//div[@id='content']/h1/span[@property='v:itemreviewed']/text()").extract()
        item['type'] = response.xpath('//*[@id="info"]/span[5]/text()').extract()
        item['date'] = response.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"][1]/text()').extract()
        item['comment'] = response.xpath("//div[@class='rating_sum']/a[@class='rating_people']/span/text()").extract()
        item['score'] = response.xpath("//div[@class='rating_self clearfix']/strong[@class='ll rating_num']/text()").extract()
        item['time_long'] = response.xpath('//span[@property="v:runtime"]/text()').extract()
        item['director'] = response.xpath('//*[@id="info"]/span[1]/span[2]/a/text()').extract()
        item['link'] = response.url

        yield item

