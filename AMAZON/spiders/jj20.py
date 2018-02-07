# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from AMAZON.items import Jj20Item
from scrapy.spiders import CrawlSpider
class Jj20Spider(scrapy.Spider):
    name = 'jj20'
    allowed_domains = ['www.jj20.com']
    start_urls = ['http://www.jj20.com/']

    custom_settings = {
    }

    def start_requests(self):
        url ='http://www.jj20.com/bz/ktmh/'
        # yield Request(url,callback=self.parser_index)

    def parser_index(self,response):
        from scrapy.http.response.html import  HtmlResponse
        # HtmlResponse.text

        new_urls = response.xpath('//ul[@class="pic2 vvi fix"]/li/a[1]/@href').extract()
        print("主页总共有%s个图组"%len(new_urls))
        for url in new_urls:
            new_url = response.urljoin(url)
            print(new_url)
            # yield Request(new_url,callback=self.parse_detail)
        # next_url = response.xpath('//a[text()="下一页"]/@href').extract_first()
        # print("下一页",next_url)
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield Request(next_url, callback=self.parser_index)




    def parse_detail(self, response):

        #Request对象
        next_img_page = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        next_img_page =response.urljoin(next_img_page)
        # print("下一张图片url = %s"%next_img_page)
        yield Request(next_img_page,callback=self.parse_detail)

        #item对象
        img_title = response.xpath('//body/div[3]/h1/span/text()').extract_first()
        # img_url = response.xpath('//div[@class="photo"]//img/@src').extract_first()
        img_url = response.xpath('//img[@id="bigImg"]/@src').extract_first()
        text ='''
        图片名：%s
        图片url：%s
        '''%(img_title,img_url)
        print(text)
        items = Jj20Item()
        items["title"] = img_title
        items["url"] = img_url
        yield items


