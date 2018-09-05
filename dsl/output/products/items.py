import scrapy

class Televizor(scrapy.Item):
	naziv = scrapy.Field(optional=True)
	cena = scrapy.Field(optional=True)
	url = scrapy.Field(optional=True)
	dijagonala = scrapy.Field(optional=True)
	ekran = scrapy.Field(optional=True)
	boja = scrapy.Field(optional=True)
	rezolucija = scrapy.Field(optional=True)
	zvucnici = scrapy.Field(optional=True)
