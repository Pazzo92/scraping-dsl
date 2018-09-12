import scrapy

class Poslanik(scrapy.Item):
	ime = scrapy.Field(optional=True)
	prezime = scrapy.Field(optional=True)
	datum_rodenja = scrapy.Field(optional=True)
	mesto_prebivalista = scrapy.Field(optional=True)
	poslanicki_klub = scrapy.Field(optional=True)
	zanimanje = scrapy.Field(optional=True)
	biografija = scrapy.Field(optional=True)
	broj_govora = scrapy.Field(optional=True)
	broj_predlozenih_zakona = scrapy.Field(optional=True)
	broj_podnetih_amandmana = scrapy.Field(optional=True)
	broj_usvojenih_amandmana = scrapy.Field(optional=True)
