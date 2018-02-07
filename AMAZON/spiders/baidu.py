# from scrapy.spider import Spider
import scrapy
from scrapy import Request
class BaiduSpider(scrapy.Spider):
    name ="baidu"
    allowed_domains =["www.baidu.com"]
    start_urls=["https://www.baidu.com"]

    def start_requests(self):
        url = "https://www.baidu.com/s?wd=minapp"
        obj1 = Request(url,self.parse,meta={"a":1})
        obj2 = Request(url,self.parse,meta={"a":1})
        return [obj1,obj2]

    def parse(self, response):
        print("解析   ",len(response.body))
        print(response.meta)

