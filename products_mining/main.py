import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'gigatron_laptops'])

if  __name__ =='__main__':
    main()