# -*- coding: utf-8 -*-
import scrapy


class AmaSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.cn/login']
    def start_requests(self):
        for s in self.start_urls:
            yield scrapy.Request(s,meta={'selenium':True},callback=self.parse,dont_filter=True)

    def parse(self, response):
        yield scrapy.Request(url='https://www.amazon.cn/gp/css/order-history/ref=nav__gno_yam_yrdrs',callback=self.login_status,dont_filter=True)

    def login_status(self,response):
        # print(response.text)
        # 输出订单时间、价格和订单编号
        times = response.xpath('.//span[@class="a-color-secondary value"]/text()').extract()
        for time in times:
            print(time.strip())
