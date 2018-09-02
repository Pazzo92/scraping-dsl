import scrapy.cmdline

def main():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'winwin_laptop'])

if  __name__ =='__main__':
    main()