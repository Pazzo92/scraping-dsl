import scrapy
import re
import unicodedata
from products.items import Movie
import products.spiders.movie_type as custom_module
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
		
		title = response.css("div.title_wrapper h1::text")
		
		if "Movie_title" in dir(custom_module):
			movie['title']= getattr(custom_module, 'Movie_title')(title)
		else:
			movie['title'] = title.extract_first()
			
		
		year = response.css("div.title_wrapper h1 span#titleYear a::text")
		
		if "Movie_year" in dir(custom_module):
			movie['year']= getattr(custom_module, 'Movie_year')(year)
		else:
			movie['year'] = year.extract_first()
			
		
		rating = response.css("div.ratingValue strong span::text")
		
		if "Movie_rating" in dir(custom_module):
			movie['rating']= getattr(custom_module, 'Movie_rating')(rating)
		else:
			movie['rating'] = rating.extract_first()
			
		
		duration = response.css("div.subtext time::text")
		
		if "Movie_duration" in dir(custom_module):
			movie['duration']= getattr(custom_module, 'Movie_duration')(duration)
		else:
			movie['duration'] = duration.extract_first()
			
		
		genre = response.css("div.subtext a::text")
		
		if "Movie_genre" in dir(custom_module):
			movie['genre']= getattr(custom_module, 'Movie_genre')(genre)
		else:
			movie['genre'] = genre.extract_first()
			
		
		release_date = response.css("div.subtext a::text")
		
		if "Movie_release_date" in dir(custom_module):
			movie['release_date']= getattr(custom_module, 'Movie_release_date')(release_date)
		else:
			movie['release_date'] = release_date.extract_first()
			
		
		story_line = response.css("div.plot_summary div.summary_text::text")
		
		if "Movie_story_line" in dir(custom_module):
			movie['story_line']= getattr(custom_module, 'Movie_story_line')(story_line)
		else:
			movie['story_line'] = story_line.extract_first()
			
		
		director = response.css("div.credit_summary_item a::text")
		
		if "Movie_director" in dir(custom_module):
			movie['director']= getattr(custom_module, 'Movie_director')(director)
		else:
			movie['director'] = director.extract_first()
			
		
		writers = response.css("div.credit_summary_item a::text")
		
		if "Movie_writers" in dir(custom_module):
			movie['writers']= getattr(custom_module, 'Movie_writers')(writers)
		else:
			movie['writers'] = writers.extract_first()
			
		
		cast = response.css("div.article table.cast_list")
		
		if "Movie_cast" in dir(custom_module):
			movie['cast']= getattr(custom_module, 'Movie_cast')(cast)
		else:
			movie['cast'] = cast.extract_first()
			
		yield movie
			
			