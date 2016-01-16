import scrapy

from bca_rate.items import RateItem

class BcaSpider(scrapy.Spider):
    name = "bca"
    allowed_domains = ["www.klikbca.com"]
    start_urls = [
        "http://www.klikbca.com"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//tr[td[@class="kurs"]]'):
            selTd = sel.xpath('td[@class="kurs"]/text()').extract()
            if len(selTd) >= 3:
                item = dict()
                item['currency'] = selTd[0]
                item['rate_buy'] = selTd[1]
                item['rate_sell'] = selTd[2]
                yield item