from scrapy.exceptions import DropItem
from scrapy.settings import Settings
from products import settings as my_settings
import pymongo

class ProductsMiningPipeline(object):

	dijagonala='40' 
	ekran='LED' 
	min_cena = 30000
	max_cena = 40000
	boja='Crna' 
	
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
		if(self.dijagonala.replace(' ','') not in item['dijagonala'].replace(' ','')
		or self.ekran.replace(' ','') not in item['ekran'].replace(' ','')
		or self.max_cena < float(item['cena'])
		or self.min_cena > float(item['cena'])		
		or self.boja.replace(' ','') not in item['boja'].replace(' ','')):
			raise DropItem("Failed to satisfy criteria: " % item)
		else:
			self.collection.insert(dict(item))
			return item		
