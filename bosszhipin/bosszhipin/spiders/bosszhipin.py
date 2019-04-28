from scrapy import Spider
from scrapy.http import Request
from bosszhipin.items import BosszhipinItem
from fake_useragent import UserAgent


class Boss(Spider):

    name = "bosszhipin"
    UA = UserAgent()
    headers = {"User-Agent": UA.random}

    cookies = {
                "pk": "cpc_user_sign_up",
                "regionCode": "+86",
                "account": "18238641800",
                "password":"bosszhipin123",
                "csessionId": "01bZvBjTunp1-7cmLJ_XP327jUsqTeRZ8vGQ8z6CM2IlnJ0mq2zs2daEfAx9QVEH9FHNU_4IRsML1fi8xu1gLxubRaw0PQ_P82ngn5nI-K9789RIXN4to0neWUzsIbDazwO6r7-VsUlMvTHPggZLfjDODUma2ZVFKNrDPSAPwY6B0",
                "csig": "05XqrtZ0EaFgmmqIQes-s-CC8Rii3iO-isqdlCc_VTpir5U2Yi8FSmW63pMMIJrYpK3dMZieWDGAQyGY5aZy6Z35JKpmMPkh1YHSqbwM8nVPQCh2CzThIlabXEunLMYg_ez1J0Cuar9dYgRvE1V1fjn-Tr9VoovGR4zpyL_nXelloDIEMjbJGo-OIdfUmRwz8eTEMQv-7ldcZ1zjAlrXc_CGN8UaNtIZWAwGEKcb6i2MmmJeerbpcc0DqUP49YHU4aXTGpIC_b_KsjDdvtEiHRbcsMXXm4kpMzUn0uKoXs0Yex3P9My-fhB2zZtdAGZDvSG-OKIs1pGGVU-kCO58MJw0iO9uE4UwnWabqWtq4gwHkfEFYEqX695Z03j09SS1vgd1r2ltfBScI7iPLemFiBbw",
                "ctoken":"BOSS_PC:1540906022146:0.ddfd15918aa33",
                "cscene": "nc_login",
                "cappKey": "FFFF0N00000000006DC1"
                                                                }

    def start_requests(self):

        ls = []
        url_ls = []
        for i in range(1, 11):
            ls = [i, i]
            url_shanghai = "https://www.zhipin.com/c101020100/?query=python&page=%s&ka=page-%s" %(ls[0], ls[1])
            url_ls.append(url_shanghai)
            url_beijing = "https://www.zhipin.com/c101010100/?query=python&page=%s&ka=page-%s" %(ls[0], ls[1])
            url_ls.append(url_beijing)
        for url in url_ls:
            yield Request(url, headers=self.headers, encoding="utf-8", cookies=self.cookies)

    def parse(self, response):
        next_url_ls = response.xpath("//div[@class='info-primary']/h3[@class='name']/a/@href").extract()
        for next_url in next_url_ls:
            next_url = "https://www.zhipin.com" + next_url
            yield Request(next_url, headers=self.headers, callback=self.detail, encoding="utf-8", cookies=self.cookies)

    def detail(self, response):
        item = BosszhipinItem()
        item['skill'] = response.xpath("//div[@class='job-sec'][1]/div[@class='text']/text()").extract()
        item['nature'] = response.xpath("//div[@class='info-company']/p/a/text()").extract()
        item['company'] = response.xpath("//div[@class='info-company']/h3[@class='name']/a/text()").extract()
        item['salary'] = response.xpath("//span[@class='badge']/text()").extract()
        item['job'] = response.xpath("//div[@class='name']/h1/text()").extract()
        item['exp'] = response.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/p").extract()
        yield item