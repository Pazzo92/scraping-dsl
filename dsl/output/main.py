import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'gigatron_Laptop'])
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'winwin_Laptop'])

if  __name__ =='__main__':
    main()