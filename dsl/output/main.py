from scrapy.crawler import CrawlerProcess
from products.spiders.spider_winwin import WinwinMobilni_telefonSpider
from products.spiders.spider_gigatron import GigatronMobilni_telefonSpider
from scrapy.settings import Settings
from products import settings as my_settings

def crawl():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(WinwinMobilni_telefonSpider)
    process.crawl(GigatronMobilni_telefonSpider)
    process.start()
    
if  __name__ =='__main__':
    crawl()