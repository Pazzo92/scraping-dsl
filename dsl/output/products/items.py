import scrapy

class Frizider(scrapy.Item):
	tip = scrapy.Field(optional=True)
	kapacitet_frizidera = scrapy.Field(optional=True)
	cena = scrapy.Field(optional=True)
	naziv = scrapy.Field(optional=True)
	sirina = scrapy.Field(optional=True)
	visina = scrapy.Field(optional=True)
	dubina = scrapy.Field(optional=True)
	energetski_razred = scrapy.Field(optional=True)
	potrosnja = scrapy.Field(optional=True)
	boja = scrapy.Field(optional=True)
