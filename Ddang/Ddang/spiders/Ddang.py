import scrapy
from scrapy.http import Request
from Ddang.items import DdangItem


class DdangSpider(scrapy.Spider):
    name = "Ddang"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}

    def start_requests(self):
        start_url = ["http://category.dangdang.com/pg{}-cp01.54.00.00.00.00.html".format(i) for i in range(2, 101)]
        for url in start_url:
            yield Request(url, headers=self.headers, encoding='GB2312')

    def parse(self, response):
        item = DdangItem()

        item["title"] = response.xpath('//p[@class="name"]/a[@title]/text()').extract()
        item["price"] = response.xpath('//p[@class="price"]/span[@class="search_now_price"]/text()').extract()
        item["publish"] = response.xpath("//p[5]/span[3]/a/text()").extract()
        item["comment"] = response.xpath("//p[4]/a/text()").extract()
        item['link'] = response.xpath("//p[@class='name']/a/@href").extract()
        yield item

