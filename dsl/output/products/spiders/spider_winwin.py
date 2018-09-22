import scrapy
import re
import unicodedata
import products.spiders.frizider_type_winwin as custom_module
from products.items import Frizider
class WinwinFriziderSpider(scrapy.Spider):
	name = "winwin_frizider"
	
	def start_requests(self):
		url = self.winwin_dictionary('frizider')
		return [scrapy.Request(url, callback=self.container_page)]
		
# function that finds all the records and enters each
	def container_page(self,response):
		links = response.xpath("//*/h2[@class='product-name']/a/@href").extract()
		for link in links:
			yield scrapy.Request(link)	
		
		next_page = response.xpath("//*/a[@class='next i-next']/@href").extract_first()
		if next_page is not None:
			yield scrapy.Request(next_page, callback=self.container_page)

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
		
		cena = response.css("div.price-box span.price::text")
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

		
		table = response.css("div.product-panels-content table.data-table")
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
					
	def winwin_dictionary(self, x):
			return {
			'laptop': 'https://www.winwin.rs/laptop-i-tablet-racunari/laptop-notebook-racunari.html',
			'tablet': 'https://www.winwin.rs/laptop-i-tablet-racunari/tablet-pc-apple-ipad/tablet.html',
			'racunar': 'https://www.winwin.rs/racunari-i-komponente/desktop-racunari/desktop-racunari-bez-os.html',
			'procesor': 'https://www.winwin.rs/racunari-i-komponente/racunarske-komponente/procesori.html',
        	'maticna_ploca': 'https://www.winwin.rs/racunari-i-komponente/racunarske-komponente/maticne-ploce.html',
        	'memorija': 'https://www.winwin.rs/racunari-i-komponente/racunarske-komponente/ram-memorije.html',
        	'hard_disk': 'https://www.winwin.rs/racunari-i-komponente/racunarske-komponente/hdd-ssd-i-oprema/interni-hard-diskovi.html',
        	'SSD': 'https://www.winwin.rs/racunari-i-komponente/racunarske-komponente/hdd-ssd-i-oprema/ssd-diskovi.html',
        	'monitor' : 'https://www.winwin.rs/pc-periferije-monitori/monitori.html',
        	'tastatura' : 'https://www.winwin.rs/pc-periferije-monitori/tastature-i-misevi/tastature.html',
        	'mis': 'https://www.winwin.rs/pc-periferije-monitori/tastature-i-misevi/misevi.html',
        	'slusalice' : 'https://www.winwin.rs/pc-periferije-monitori/slusalice-i-mikrofoni.html',
        	'memorijska_kartica' : 'https://www.winwin.rs/mobilni-i-fiksni-telefoni/mobilni-telefoni/memorijske-kartice.html', 
        	'USB_flash' : 'https://www.winwin.rs/pc-periferije-monitori/usb-flash-memorije.html',
        	'stampac' : 'https://www.winwin.rs/stampaci-office/stampaci/laserski-stampaci.html',
        	'skener' : 'https://www.winwin.rs/stampaci-office/skeneri.html',
        	'sony' : 'https://www.winwin.rs/gaming-igrice-konzole/konzole-i-oprema/konzole-za-igranje.html?manufacturer=56205y',
        	'xbox' : 'https://www.winwin.rs/gaming-igrice-konzole/konzole-i-oprema/konzole-za-igranje.html?manufacturer=54921',
        	'nintendo' : 'https://www.winwin.rs/gaming-igrice-konzole/konzole-i-oprema/konzole-za-igranje.html?manufacturer=55155',
        	'televizor' : 'https://www.winwin.rs/tv-audio-video/tv/televizori.html',
        	'mrezna_karta' : 'https://www.winwin.rs/mreze-sigurnosna-oprema/mrezne-kartice.html',
        	'ruter' : 'https://www.winwin.rs/mreze-sigurnosna-oprema/switch-i-ruter/lan-ruter.html',
        	'mobilni_telefon' : 'https://www.winwin.rs/mobilni-i-fiksni-telefoni/mobilni-telefoni/smart-mobilni-telefoni.html',
        	'telefon' : 'https://www.winwin.rs/mobilni-i-fiksni-telefoni/fiksni-telefoni/bezicni-telefoni.html',
        	'frizider' : 'https://www.winwin.rs/bela-tehnika/rashladni-uredaji/frizideri.html',
        	'zamrzivac' : 'https://www.winwin.rs/bela-tehnika/rashladni-uredaji/zamrzivaci.html',
        	'masina_za_ves' : 'https://www.winwin.rs/bela-tehnika/ves-masine/masine-za-pranje-vesa.html',
        	'sporet' : 'https://www.winwin.rs/bela-tehnika/sporeti-i-mikrotalasne/sporeti.html',
        	'mikrotalasne' : 'https://www.winwin.rs/bela-tehnika/sporeti-i-mikrotalasne/mikrotalasne-rerne.html',
        	'klima_uredjaj' : 'https://www.winwin.rs/bela-tehnika/klima-uredaji/klime.html',
        	'bojler' : 'https://www.winwin.rs/bela-tehnika/bojleri.html',
        	'fotoaparat' : 'https://www.winwin.rs/foto-oprema/digitalni-fotoaparati.html',
        	'gitara' : 'https://www.winwin.rs/tv-audio-video/muzicki-instrumenti-i-oprema.html?tip_filter=65211'		
			}.get(x, '')  
			