import scrapy

class Gitara(scrapy.Item):
	url = scrapy.Field(optional=True)
	tip = scrapy.Field(optional=True)
	telo = scrapy.Field(optional=True)
	cena = scrapy.Field(optional=True)
	naziv = scrapy.Field(optional=True)
	vrat = scrapy.Field(optional=True)
	boja = scrapy.Field(optional=True)
	opis = scrapy.Field(optional=True)
	model = scrapy.Field(optional=True)
	boja = scrapy.Field(optional=True)
