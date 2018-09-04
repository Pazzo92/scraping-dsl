from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	procesor='Intel Core i5' 
	ekran='15.6' 
	min_cena = 50000
	max_cena = 90000
	memorija='8' 
	graficka='GeForce' 
	
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
		if(self.procesor.replace(' ','') not in item['procesor'].replace(' ','')
		or self.ekran.replace(' ','') not in item['ekran'].replace(' ','')
		or self.max_cena < float(item['cena'])
		or self.min_cena > float(item['cena'])		
		or self.memorija.replace(' ','') not in item['memorija'].replace(' ','')
		or self.graficka.replace(' ','') not in item['graficka'].replace(' ','')):
			raise DropItem("Failed to satisfy criteria: " % item)
		else:
			self.collection.insert(dict(item))
			return item		
