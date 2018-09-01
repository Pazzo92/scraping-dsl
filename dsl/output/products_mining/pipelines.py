from scrapy.exceptions import DropItem

class ProductsMiningPipeline(object):

	procesor='Intel Core i3' 
	ekran='14 HD LED' 
	max_cena = 30000
	min_cena = 50000
		
	def process_item(self, item, spider):
		if(self.procesor not in item['procesor']
		or self.ekran not in item['ekran']
		or self.max_cena < float(item['cena'])
		or self.min_cena > float(item['cena)'])):
			raise DropItem("Failed to satisfy criteria: " % item)
		else:
			return item		
