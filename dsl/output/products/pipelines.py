from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	poslanicki_klub='Dosta je bilo' 
	
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
		if(self.poslanicki_klub.replace(' ','').lower() not in item['poslanicki_klub'].replace(' ','').lower()):
				raise DropItem("Failed to satisfy criteria: " % item)
		self.collection.insert(dict(item))
		return item	