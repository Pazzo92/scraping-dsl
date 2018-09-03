import scrapy
from products.items import Laptop
import re
import unicodedata

class WinwinLaptopSpider(scrapy.Spider):
	name = "winwin_Laptop"
	
	def start_requests(self):
		url = self.winwin_dictionary('laptop')
		return [scrapy.Request(url, callback=self.parse_links)]
		
	def parse_links(self,response):
		links = response.xpath("//*/h2[@class='product-name']/a/@href").extract()
		for link in links:
			yield scrapy.Request('https://www.winwin.rs/laptop-i-tablet-racunari/laptop-notebook-racunari/laptop-hp-pavilion-14-bk008nm-2nq60ea-14-fhd-intel-i5-7200u-8gb-1tb-gf-940mx-2-gb-hdm-8612215.html')	
		
	#	next_page = response.xpath("//*/a[@class='next i-next']/@href").extract_first()
	#	if next_page is not None:
	#		yield scrapy.Request(next_page, callback=self.parse_links)
		
	def parse(self,response):
		
		laptop = Laptop()
		
		properties_list = []
		properties_list.append('procesor')
		properties_list.append('ekran')
		laptop['cena'] = response.css('div.price-box span.price::text').extract_first().strip()[:-5].replace(".","")
		laptop['naziv'] = response.css('h1::text').extract_first()
		properties_list.append('memorija')
		properties_list.append('baterija')
		properties_list.append('operativni_sistem')
		properties_list.append('graficka')
		
		table = response.css('div.product-panels-content table.data-table')
		for tr in table.css('tr'):
			name = tr.css('th::text').extract_first().strip()
			value = tr.css('td::text').extract_first()
			
			if value is not None and name is not None:
				value = unicodedata.normalize('NFD', value).encode('ascii', 'ignore').decode('utf-8')
				name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf-8')
				
			for property in properties_list:
				if property == name.lower():
					laptop[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
				elif property in name.lower():
					print(not laptop[property])
					laptop[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
				elif '_' in property:
					if property == name.lower().replace(' ','_'):
						laptop[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
		
		yield laptop
					
	def winwin_dictionary(self, x):
			return {
			'laptop': 'https://www.winwin.rs/laptop-i-tablet-racunari/laptop-notebook-racunari.html'
			}.get(x, '')  