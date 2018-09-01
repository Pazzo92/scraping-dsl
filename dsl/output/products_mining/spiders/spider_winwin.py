import scrapy
from products_mining.items import Laptop

class WinwinLaptopSpider(scrapy.Spider):
	name = "winwin_Laptop"
	
	def start_requests(self):
		url = self.winwin_dictionary('laptop')
		return [scrapy.Request(url, callback=self.get_number_of_items)]
		
	def parse_links(self,response):
		links = response.xpath("//*/h2[@class='product-name']/a/@href").extract()
		for link in links:
			return [scrapy.Request(link)]	
		
		next_page = response.xpath("//*/a[@class='next i-next']/@href").extract_first()
		if next_page is not None:
			return [scrapy.Request(next_page, callback=self.parse_links)]
		
	def parse(self,response):
		
		laptop = Laptop()
		
		properties_list = []
		properties_list.append('procesor')
		properties_list.append('ekran')
		laptop['cena'] = response.css('div.price-box span.price::text').extract_first().strip()
		laptop['naziv'] = response.css('h1::text').extract_first()
		
		table = response.css('div.product-panels-content table.data-table')
		for tr in table.css('tr'):
			name = tr.css('th::text').extract_first().strip()
			value = tr.css('td::text').extract_first().strip()
			
			for property in properties_list:
				if property == name.lower():
					laptop[name] = value
					
		def winwin_dictionary(self, x):
			return {
			'laptop': 'https://www.winwin.rs/laptop-i-tablet-racunari/laptop-notebook-racunari.html'
			}.get(x, '')  