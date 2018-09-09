import scrapy
import re
import unicodedata
from products.items import Movie
class MovieSpider(scrapy.Spider):
	name = "movie"
	
# start page
	def start_requests(self):
		url = "https://www.imdb.com/chart/top?ref_=nv_mv_250"
		return [scrapy.Request(url, callback=self.main_page)]
			
# function that finds all records needed
	def main_page(self,response):	
		links = response.css("table.chart.full-width tbody")
		for link in links.css("tr"):
			yield scrapy.Request("https://www.imdb.com"+ link.css("td.titleColumn a::attr(href)").extract_first())
	
# main function that parses single entity		
	def parse(self,response):
		movie = Movie()
		properties_list = []
		aliases_dict = {}
		movie['title'] = response.css('div.title_wrapper h1::text').extract_first().strip()
		movie['year'] = response.css('div.title_wrapper h1 span#titleYear a::text').extract_first().strip()
		movie['rating'] = response.css('div.ratingValue strong span::text').extract_first()
		movie['duration'] = response.css('div.subtext time::text').extract_first().strip()
		movie['genre'] = ", ".join(response.css('div.subtext a::text').extract()[:-1])
		movie['release_date'] = response.css('div.subtext a::text').extract()[-1].strip()
		movie['storyline'] = response.css('div.plot_summary div.summary_text::text').extract_first().strip()
		movie['director'] = response.css('div.credit_summary_item a::text').extract()[0]
		movie['writers'] = response.css('div.credit_summary_item a::text').extract()[1]
		cast = []
		table = response.css('div.article table.cast_list')
		for tr in table.css('tr'):
			actor = tr.css('td a::text').extract_first() 
			if actor is not None:
				cast.append(actor.strip())
		movie['cast'] = ', '.join(cast)
		
		yield movie
			
			