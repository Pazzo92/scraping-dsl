import scrapy
from products.items import Gitara
import re
import unicodedata

class GigatronGitaraSpider(scrapy.Spider):
	name = "gigatron_Gitara"
	
	def start_requests(self):
		url = self.gigatron_dictionary('gitara')
		return [scrapy.Request(url, callback=self.get_number_of_items)]
		
	def get_number_of_items(self, response):
		number_of_items = response.css('b#total::text').extract_first()
		return [scrapy.Request(response.request.url+ '?limit=' + number_of_items, callback=self.parse_links)]
	 
	def parse_links(self,response):
		links = response.xpath("//*/h4/a[@class='product-name']/@href").extract()
		for link in links:
			yield scrapy.Request(link)
		
	def parse(self,response):
		
		gitara = Gitara()
		
		properties_list = []
		gitara['url'] = response.request.url
	
		properties_list.append('tip')
	
		properties_list.append('telo')
		gitara['cena'] = response.css('div.price-item.currency-item h5::text').extract_first().strip().replace(".","")
		gitara['naziv'] = response.css('h1::text').extract_first()
	
		properties_list.append('vrat')
	
		properties_list.append('boja')
	
		properties_list.append('opis')
	
		properties_list.append('model')
	
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
					gitara[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
				elif '_' in property:
					if property == name.lower().replace(' ','_'):
						gitara[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
		
		yield gitara
			
	def gigatron_dictionary(self, x):
			return {
        	'laptop': 'https://www.gigatron.rs/laptop_racunari',
        	'tablet': 'https://www.gigatron.rs/tablet_racunari',
        	'racunar': 'https://www.gigatron.rs/gigatron_racunari',
        	'procesor': 'https://www.gigatron.rs/procesori',
        	'maticna_ploca': 'https://www.gigatron.rs/maticne_ploce',
        	'memorija': 'https://www.gigatron.rs/memorije',
        	'hard_disk': 'https://www.gigatron.rs/hard_diskovi',
        	'SSD': 'https://www.gigatron.rs/ssd',
        	'monitor' : 'https://www.gigatron.rs/monitori',
        	'tastatura' : 'https://www.gigatron.rs/tastature',
        	'mis': 'https://www.gigatron.rs/misevi',
        	'slusalice' : 'https://www.gigatron.rs/slusalice',
        	'memorijska_kartica' : 'https://www.gigatron.rs/memorijske_kartice', 
        	'USB_flash' : 'https://www.gigatron.rs/usb_flash_memorija',
        	'stampac' : 'https://www.gigatron.rs/stampaci',
        	'skener' : 'https://www.gigatron.rs/skeneri',
        	'sony' : 'https://www.gigatron.rs/sony',
        	'xbox' : 'https://www.gigatron.rs/xbox',
        	'nintendo' : 'https://www.gigatron.rs/nintendo',
        	'televizor' : 'https://www.gigatron.rs/televizori',
        	'mrezna_karta' : 'https://www.gigatron.rs/mrezne_karte_i_adapteri',
        	'ruter' : 'https://www.gigatron.rs/ruteri',
        	'mobilni_telefon' : 'https://www.gigatron.rs/mobilni_telefoni',
        	'telefon' : 'https://www.gigatron.rs/telefoni',
        	'frizider' : 'https://www.gigatron.rs/frizideri',
        	'zamrzivac' : 'https://www.gigatron.rs/zamrzivaci',
        	'masina_za_ves' : 'https://www.gigatron.rs/masine_za_ves',
        	'sporet' : 'https://www.gigatron.rs/sporeti_ploce_i_rerne',
        	'mikrotalasne' : 'https://www.gigatron.rs/mikrotalasne_rerne',
        	'klima_uredjaj' : 'https://www.gigatron.rs/klima_uredjaji_i_oprema',
        	'bojler' : 'https://www.gigatron.rs/bojleri',
        	'fotoaparat' : 'https://www.gigatron.rs/digitalni_fotoaparati',
        	'gitara' : 'https://www.gigatron.rs/gitare'
        	}.get(x, '')
        	
        