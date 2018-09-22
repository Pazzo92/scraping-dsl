from scrapy.crawler import CrawlerProcess
from products.spiders.spider_winwin import WinwinFriziderSpider
from products.spiders.spider_gigatron import GigatronFriziderSpider
from scrapy.settings import Settings
from products import settings as my_settings

def crawl():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(WinwinFriziderSpider)
    process.crawl(GigatronFriziderSpider)
    process.start()
    
if  __name__ =='__main__':
    crawl()