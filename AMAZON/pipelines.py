# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from pymongo import MongoClient
#自定义Pipeline
class CustomPipeline(object):
    def __init__(self,host,port,db,collection,user,pwd):
        self.host = host
        self.port = port
        self.db = db
        self.collection = collection
        self.user = user
        self.pwd = pwd

    @classmethod
    def from_crawler(cls, crawler):
        """
        Scrapy会先通过getattr判断我们是否自定义了from_crawler,有则调它来完
        成实例化
        """
        port = crawler.settings.getint('PORT')
        host = crawler.settings.get('HOST')
        collection = crawler.settings.get('COLLECTION')
        db = crawler.settings.get('DB')
        user = crawler.settings.get('USER')
        pwd = crawler.settings.get('PWD')
        return cls(host,port,db,collection,user,pwd)

    def open_spider(self,spider):
        """
        爬虫刚启动时执行一次
        """
        print('刚启动时执行一次')
        self.client = MongoClient("mongodb://%s:%s@%s:%s"%(self.user,self.pwd,self.host,self.port))

    def close_spider(self,spider):
        """
        爬虫关闭时执行一次
        """
        print('关闭时执行一次')
        self.client.close()


    def process_item(self, item, spider):
        # 操作并进行持久化

        # return表示会被后续的pipeline继续处理
        # return item

        # 表示将item丢弃，不会被后续pipeline处理
        item_dic = dict(item)
        if all(item_dic.values()):
            self.client[self.db][self.collection].save(item_dic)
        raise DropItem()