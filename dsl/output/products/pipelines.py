from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	procesor='Intel Core i3-7130U' 
	ekran='15.6' 
	min_cena = 30000
	max_cena = 50000
	
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
		if(self.procesor not in item['procesor']
		or self.ekran not in item['ekran']
		or self.max_cena < float(item['cena'])
		or self.min_cena > float(item['cena'])):
			raise DropItem("Failed to satisfy criteria: " % item)
		else:
			self.collection.insert(dict(item))
			return item		
