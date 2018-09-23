import scrapy

class Movie(scrapy.Item):
	title = scrapy.Field(optional=True)
	year = scrapy.Field(optional=True)
	rating = scrapy.Field(optional=True)
	duration = scrapy.Field(optional=True)
	genre = scrapy.Field(optional=True)
	release_date = scrapy.Field(optional=True)
	story_line = scrapy.Field(optional=True)
	director = scrapy.Field(optional=True)
	writers = scrapy.Field(optional=True)
	cast = scrapy.Field(optional=True)
