import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'winwin_laptops'])

if  __name__ =='__main__':
    main()