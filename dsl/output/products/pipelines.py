from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	opis_procesora='Octa-core' 
	procesor='Octa-core' 
	interna_memorija='64GB' 
	min_cena = 60000
	max_cena = 80000
	operativni_sistem='Android' 
	
	def __init__(self):
		settings = Settings()
		settings.setmodule(my_settings)
		connection = pymongo.MongoClient(
			settings['MONGODB_SERVER'],
			settings['MONGODB_PORT']
		)
		db = connection[settings['MONGODB_DB']]
		self.collection = db[settings['MONGODB_COLLECTION']]
	
	def process_item(self, item, spider):
		try:
			if(self.opis_procesora.replace(' ','') not in item['opis_procesora'].replace(' ','')):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		try:
			if(self.procesor.replace(' ','') not in item['procesor'].replace(' ','')):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		try:
			if(self.interna_memorija.replace(' ','') not in item['interna_memorija'].replace(' ','')):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		try:
			if(self.max_cena < float(item['cena'])):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		try:
			if(self.min_cena > float(item['cena'])):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		try:
			if(self.operativni_sistem.replace(' ','') not in item['operativni_sistem'].replace(' ','')):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		self.collection.insert(dict(item))
		return item	