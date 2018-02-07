# -*- coding: utf-8 -*-

# Scrapy settings for AMAZON project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AMAZON'

SPIDER_MODULES = ['AMAZON.spiders']
NEWSPIDER_MODULE = 'AMAZON.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AMAZON (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # robot 网站告诉那些可爬取内容那些不能爬取的内容，放进robot文件

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3   #添加爬虫程序的间隔时间，防止大量请求导致网站奔溃
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers: #所有爬虫程序，可共用headers
DEFAULT_REQUEST_HEADERS = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html # 爬虫中间件，如果自定义则需修改这里
#SPIDER_MIDDLEWARES = {
#    'AMAZON.middlewares.AmazonSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html # 下载中间件，如果自定义则需修改这里
DOWNLOADER_MIDDLEWARES = {
   # 'AMAZON.middlewares.MyCustomDownloaderMiddleware': 543, #后面数字代表优先级，1~1000   1最高，1000最低
   'AMAZON.middlewares.DownMiddleware1': 543, #后面数字代表优先级，1~1000   1最高，1000最低

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html  # piplines 数据持久化操作类
ITEM_PIPELINES = {
   # 'AMAZON.pipelines.AmazonPipeline': 300,
   'AMAZON.pipelines.CustomPipeline': 200, #自定义的PIPELINES
}


DB="amazon"
COLLECTION="pic"
HOST="localhost"
PORT=27017
USER="root"
PWD="123"

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# DUPEFILTER_CLASS = '' #自定义去重类