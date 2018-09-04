import scrapy

class Laptop(scrapy.Item):
	procesor = scrapy.Field()
	ekran = scrapy.Field()
	cena = scrapy.Field()
	naziv = scrapy.Field()
	memorija = scrapy.Field()
	baterija = scrapy.Field()
	operativni_sistem = scrapy.Field()
	graficka = scrapy.Field()
	boja = scrapy.Field()
