import scrapy

class Mobilni_telefon(scrapy.Item):
	rezolucija = scrapy.Field(optional=True)
	operativni_sistem = scrapy.Field(optional=True)
	cena = scrapy.Field(optional=True)
	naziv = scrapy.Field(optional=True)
	interna_memorija = scrapy.Field(optional=True)
	procesor = scrapy.Field(optional=True)
	opis_procesora = scrapy.Field(optional=True)
	ram_memorija = scrapy.Field(optional=True)
	radna_memorija = scrapy.Field(optional=True)
	kamera = scrapy.Field(optional=True)
	procesor = scrapy.Field(optional=True)
	url = scrapy.Field(optional=True)
