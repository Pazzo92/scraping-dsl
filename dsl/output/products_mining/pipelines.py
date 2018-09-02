from scrapy.exceptions import DropItem
from scrapy.conf import settings
import pymongo

class ProductsMiningPipeline(object):

	procesor='Intel Core i3' 
	ekran='14 HD LED' 
	max_cena = 30000
	min_cena = 50000
	
	def __init__(self):
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
		or self.min_cena > float(item['cena)'])):
			raise DropItem("Failed to satisfy criteria: " % item)
		else:
			self.collection.insert(dict(item))
			return item		
