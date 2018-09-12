import scrapy
import re
import unicodedata
from products.items import Poslanik
class PoslanikSpider(scrapy.Spider):
	name = "poslanik"
	
# start page
	def start_requests(self):
		url = "http://www.otvoreniparlament.rs/poslanik"
		return [scrapy.Request(url, callback=self.container_page)]
		
# function that finds all the records
	def container_page(self,response):
		links = response.xpath("//*/h3[@class='card-title']/a/@href").extract()
		for link in links:
			yield scrapy.Request(link, callback = self.main_page)
			
# function that enters record needed
	def main_page(self,response):	
		links = response.xpath("//*/h4[@class='media-heading']/a/@href").extract()
		for link in links:
			yield scrapy.Request(link)
			
# main function that parses single entity		
	def parse(self,response):
		poslanik = Poslanik()
		properties_list = []
		aliases_dict = {}
		poslanik['ime'] = response.css('div.row div.col-xs-12 h2.page-heading.text-center.text-uppercase::text').extract_first().strip().split(' ')[0].lower().capitalize()
		poslanik['prezime'] = response.css('div.row div.col-xs-12 h2.page-heading.text-center.text-uppercase::text').extract_first().strip().split(' ')[2].lower().capitalize()
		properties_list.append('datum_rodenja')
		aliases = []
		aliases_dict['datum_rodenja'] = aliases
		properties_list.append('mesto_prebivalista')
		aliases = []
		aliases_dict['mesto_prebivalista'] = aliases
		properties_list.append('poslanicki_klub')
		aliases = []
		aliases_dict['poslanicki_klub'] = aliases
		properties_list.append('zanimanje')
		aliases = []
		aliases_dict['zanimanje'] = aliases
		properties_list.append('broj_govora')
		aliases = []
		aliases_dict['broj_govora'] = aliases
		properties_list.append('broj_predlozenih_zakona')
		aliases = []
		aliases_dict['broj_predlozenih_zakona'] = aliases
		properties_list.append('broj_podnetih_amandmana')
		aliases = []
		aliases_dict['broj_podnetih_amandmana'] = aliases
		properties_list.append('broj_usvojenih_amandmana')
		aliases = []
		aliases_dict['broj_usvojenih_amandmana'] = aliases
		
		table = response.css('div.card-content ul')
		for li in table.css('li'):
			name = li.css('label::text').extract_first().strip().replace(':','')
			link = li.css('a::text').extract_first()
			if link is not None:
				value = link.strip()
			else:
				value = li.css('::text').extract()
				for line in value:
					value = line.strip()
			
			if name is not None:
				name = unicodedata.normalize('NFD', name).encode('ascii', 'ignore').decode('utf-8')
			
			for property in properties_list:
				if property == name.lower() or name.lower().replace(' ','_') in aliases_dict[property]:
					poslanik[property] = re.sub(r'[^a-zA-Z0-9.\-"ÄŒÄ†Ä�Å Å½Å¾Å¡Ä‘Ä‡Ä� ]',r'',value.strip())
				elif '_' in property:
					if property == name.lower().replace(' ','_'):
						poslanik[property] = re.sub(r'[^a-zA-Z0-9.\-"ÄŒÄ†Ä�Å Å½Å¾Å¡Ä‘Ä‡Ä� ]',r'',value.strip())
		
		yield poslanik
			
					
		biografija = response.css('div.js-eq-limit::text').extract()
		strbio = ''
		for line in biografija:
			strbio += line.strip()
		poslanik['{{prop.name}}'] = strbio
		yield poslanik