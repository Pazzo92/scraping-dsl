import scrapy
import re
import unicodedata
import products.spiders.frizider_type_gigatron as custom_module
from products.items import Frizider

class GigatronFriziderSpider(scrapy.Spider):
	name = "gigatron_frizider"
	
	def start_requests(self):
		url = self.gigatron_dictionary('frizider')
		return [scrapy.Request(url, callback=self.get_number_of_items)]

#function that retrieves and loads all the records
	def get_number_of_items(self, response):
		number_of_items = response.css('b#total::text').extract_first()
		return [scrapy.Request(response.request.url+ '?limit=' + number_of_items, callback=self.parse_links)]

# function that enters record needed
	def parse_links(self,response):
		links = response.xpath("//*/h4/a[@class='product-name']/@href").extract()
		for link in links:
			yield scrapy.Request(link)

# main function that parses single entity		
	def parse(self,response):
		
		frizider = Frizider()
		properties_list = []
		aliases_dict = {}
		
		properties_list.append('tip')
		aliases = []
		aliases_dict['tip'] = aliases
		
		properties_list.append('kapacitet_frizidera')
		aliases = []
		aliases_dict['kapacitet_frizidera'] = aliases
		
		cena = response.css("div.price-item.currency-item h5::text")
		if "Frizider_cena" in dir(custom_module):
			frizider['cena']= getattr(custom_module, 'Frizider_cena')(cena)
		else:
			frizider['cena'] = cena.extract_first()
		
		naziv = response.css("h1::text")
		if "Frizider_naziv" in dir(custom_module):
			frizider['naziv']= getattr(custom_module, 'Frizider_naziv')(naziv)
		else:
			frizider['naziv'] = naziv.extract_first()
		
		properties_list.append('sirina')
		aliases = []
		aliases_dict['sirina'] = aliases
		
		properties_list.append('visina')
		aliases = []
		aliases_dict['visina'] = aliases
		
		properties_list.append('dubina')
		aliases = []
		aliases_dict['dubina'] = aliases
		
		properties_list.append('energetski_razred')
		aliases = []
		aliases_dict['energetski_razred'] = aliases
		
		properties_list.append('potrosnja')
		aliases = []
		aliases_dict['potrosnja'] = aliases
		
		properties_list.append('boja')
		aliases = []
		aliases_dict['boja'] = aliases

		
		table = response.css("div.main.clearfix table.product-specs")
		for row in table.css("tr"):
			name = getattr(custom_module, 'Table_name')(row)
			value = getattr(custom_module, 'Table_value')(row)

			if name is not None:
				name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf-8')
			
			for property in properties_list:
				if property == name.lower() or name.lower().replace(' ','_') in aliases_dict[property]:
					frizider[property] = re.sub(r'[^a-zA-Z0-9.\-"ČĆĐŠŽžšđćč ]',r'',value.strip())
				elif '_' in property:
					if property == name.lower().replace(' ','_'):
						frizider[property] = re.sub(r'[^a-zA-Z0-9.\-"ČĆĐŠŽžšđćč ]',r'',value.strip())
		yield frizider
 
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
 	
        