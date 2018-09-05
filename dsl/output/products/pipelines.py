from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	tip='Klasicna' 
	max_cena = 45000
	
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
			if(self.tip.replace(' ','') not in item['tip'].replace(' ','')):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		try:
			if(self.max_cena < float(item['cena'])):
				raise DropItem("Failed to satisfy criteria: " % item)
		except KeyError:
				pass
		self.collection.insert(dict(item))
		return item	