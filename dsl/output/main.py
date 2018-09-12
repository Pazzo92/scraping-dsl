from scrapy.crawler import CrawlerProcess
from products.spiders.spider_poslanik import PoslanikSpider
from scrapy.settings import Settings
from products import settings as my_settings

def crawl():
    crawler_settings = Settings()
    crawler_settings.setmodule(my_settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(PoslanikSpider)
    process.start()
    
if  __name__ =='__main__':
    crawl()