import scrapy

class Televizor(scrapy.Item):
	rezolucija = scrapy.Field()
	dijagonala = scrapy.Field()
	cena = scrapy.Field()
	naziv = scrapy.Field()
	osvetljenje = scrapy.Field()
	ekran = scrapy.Field()
	boja = scrapy.Field()
	kontrast = scrapy.Field()
