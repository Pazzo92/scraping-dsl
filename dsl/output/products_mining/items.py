import scrapy

class Laptop(scrapy.Item):
	procesor = scrapy.Field()
	ekran = scrapy.Field()
	cena = scrapy.Field()
	naziv = scrapy.Field()
