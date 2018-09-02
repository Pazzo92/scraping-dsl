import scrapy
from items import Laptop

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
			return [scrapy.Request(link)]
		
	def parse(self,response):
		
		laptop = Laptop()
		
		properties_list = []
		properties_list.append('procesor')
		properties_list.append('ekran')
		laptop['cena'] = response.css('div.price-item.currency-item h5::text').extract_first().strip()
		laptop['naziv'] = response.css('h1::text').extract_first()
		
		table = response.css('div.main.clearfix table.product-specs')
		for tr in table.css('tr'):
			name = tr.css('th::text').extract_first().strip()
			link = tr.css('a::text').extract_first()
			if link is not None:
				value = link.strip()
			else:
				value = tr.css('td::text').extract_first().strip()
			
			for property in properties_list:
				if property == name.lower():
					laptop[name] = value
					
		def gigatron_dictionary(self, x):
			return {
        	'laptop': 'https://www.gigatron.rs/laptop_racunari'
        	}.get(x, '')
        	
        