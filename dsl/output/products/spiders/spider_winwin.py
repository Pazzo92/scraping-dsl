import scrapy
from products.items import Mobilni_telefon
import re
import unicodedata

class WinwinMobilni_telefonSpider(scrapy.Spider):
	name = "winwin_Mobilni_telefon"
	
	def start_requests(self):
		url = self.winwin_dictionary('mobilni_telefon')
		return [scrapy.Request(url, callback=self.parse_links)]
		
	def parse_links(self,response):
		links = response.xpath("//*/h2[@class='product-name']/a/@href").extract()
		for link in links:
			yield scrapy.Request(link)	
		
		next_page = response.xpath("//*/a[@class='next i-next']/@href").extract_first()
		if next_page is not None:
			yield scrapy.Request(next_page, callback=self.parse_links)
		
	def parse(self,response):
		
		mobilni_telefon = Mobilni_telefon()
		
		properties_list = []
		properties_list.append('rezolucija')
		properties_list.append('operativni_sistem')
		mobilni_telefon['cena'] = response.css('div.price-box span.price::text').extract_first().strip()[:-5].replace(".","")
		mobilni_telefon['naziv'] = response.css('h1::text').extract_first()
		properties_list.append('interna_memorija')
		properties_list.append('procesor')
		properties_list.append('opis_procesora')
		properties_list.append('ram_memorija')
		properties_list.append('radna_memorija')
		properties_list.append('kamera')
		properties_list.append('procesor')
		mobilni_telefon['url'] = response.request.url
		
		table = response.css('div.product-panels-content table.data-table')
		for tr in table.css('tr'):
			name = tr.css('th::text').extract_first().strip()
			value = tr.css('td::text').extract_first()
			
			if value is not None and name is not None:
				value = unicodedata.normalize('NFD', value).encode('ascii', 'ignore').decode('utf-8')
				name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf-8')
			
			for property in properties_list:
				if property == name.lower():
					mobilni_telefon[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
				elif '_' in property:
					if property == name.lower().replace(' ','_'):
						mobilni_telefon[property] = re.sub(r'[^a-zA-Z0-9.\- ]',r'',value.strip())
		
		yield mobilni_telefon
					
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