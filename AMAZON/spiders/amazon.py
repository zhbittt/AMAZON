# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from urllib.parse import urlencode
from AMAZON.items import AmazonItem
class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['www.amazon.cn']
    start_urls = ['http://www.amazon.cn/'] # 根地址，如果自己没有指定url，就访问这个url

    def __init__(self,keyword,*args,**kwargs):
        super(AmazonSpider,self).__init__(*args,**kwargs)
        self.keyword=keyword
    custom_settings={

    }


    def start_requests(self):
        '''
        程序运行只执行一次，
        :return:
        '''
        # url='https://www.amazon.cn/s/ref=nb_sb_noss_1/461-4093573-7508641?'
        # url+=urlencode({"field-keywords" : self.keyword})
        # print(url)
        url="https://www.amazon.cn/s/ref=nb_sb_ss_c_1_6?field-keywords=%E6%89%8B%E6%9C%BA"
        yield Request(url,callback=self.parse_index,dont_filter=False)


    def parse_index(self,response):
        # from scrapy.http import HtmlResponse
        goods=response.xpath('//*[contains(@id,"result_")]/div/div[3]/div[1]/a/@href').extract()
        print(goods)
        for good in goods:
            yield Request(good,callback=self.parse_detail,dont_filter=False)


    def parse_detail(self, response):

        title = response.xpath('//*[@id="productTitle"]/text()').extract_first().strip()
        price = response.xpath('//*[@id="priceblock_ourprice"]/text()').extract_first()
        delivery_method = "".join(response.xpath('//*[@id="ddmMerchantMessage"]//text()').extract())
        text = """
        ==============================================
        url=%s
        title=%s 
        price=%s
        %s
        ==============================================
        """%(response.url,title,price,delivery_method)
        print(text)
        items =AmazonItem()
        items["url"]=response.url
        items["title"]=title
        items["price"]=price
        items["delivery_method"]=delivery_method
        yield items


