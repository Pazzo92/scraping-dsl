from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	max_cena = 25000
	naziv='Gorenje' 
	min_cena = 10000
	energetski_razred='A' 
	
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
		if(self.max_cena < float(item['cena'])):
				raise DropItem("Failed to satisfy criteria: " % item)

		if(self.naziv.replace(' ','').lower() not in item['naziv'].replace(' ','').lower()):
				raise DropItem("Failed to satisfy criteria: " % item)
		if(self.min_cena > float(item['cena'])):
				raise DropItem("Failed to satisfy criteria: " % item)
		if(self.energetski_razred.replace(' ','').lower() not in item['energetski_razred'].replace(' ','').lower()):
				raise DropItem("Failed to satisfy criteria: " % item)
		self.collection.insert(dict(item))
		return item	