import scrapy
from products.items import Laptop
import re
import unicodedata

class GigatronLaptopSpider(scrapy.Spider):
	name = "gigatron_Laptop"
	
	def start_requests(self):
		url = self.gigatron_dictionary('laptop')
		return [scrapy.Request(url, callback=self.get_number_of_items)]
		
	def get_number_of_items(self, response):
		number_of_items = response.css('b#total::text').extract_first()
		return [scrapy.Request(response.request.url+ '?limit=' + number_of_items, callback=self.parse_links)]
	 
	def parse_links(self,response):
		links = response.xpath("//*/h4/a[@class='product-name']/@href").extract()
		for link in links:
			yield scrapy.Request(link)
		
	def parse(self,response):
		
		laptop = Laptop()
		
		properties_list = []
		properties_list.append('procesor')
		properties_list.append('ekran')
		laptop['cena'] = response.css('div.price-item.currency-item h5::text').extract_first().strip().replace(".","")
		laptop['naziv'] = response.css('h1::text').extract_first()
		properties_list.append('memorija')
		properties_list.append('baterija')
		properties_list.append('operativni_sistem')
		properties_list.append('graficka')
		properties_list.append('boja')
		
		table = response.css('div.main.clearfix table.product-specs')
		for tr in table.css('tr'):
			name = tr.css('th::text').extract_first().strip()
			link = tr.css('a::text').extract_first()
			if link is not None:
				value = link.strip()
			else:
				value = tr.css('td::text').extract_first()
				
			if value is not None and name is not None:
				value = unicodedata.normalize('NFD', value).encode('ascii', 'ignore').decode('utf-8')
				name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf-8')
			
			for property in properties_list:
				if property == name.lower():
					laptop[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
				elif property in name.lower():
					try:
						laptop[property]
					except KeyError:
						laptop[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
				elif '_' in property:
					if property == name.lower().replace(' ','_'):
						laptop[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
		
		yield laptop
			
	def gigatron_dictionary(self, x):
			return {
        	'laptop': 'https://www.gigatron.rs/laptop_racunari'
        	}.get(x, '')
        	
        