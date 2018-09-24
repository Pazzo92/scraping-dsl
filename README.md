# Scraping DSL

Project that is using textX to define and interpret DSL in order to generate and run Scrapy project for scraping various types of items and storing it in the MongoDB.

The project currently supports scraping top 250 movies from imdb, councils at otvoreniparlament.rs , and all the products from gigatron and winwin website. (You can find all the examples in the examples folder)

# Prerequisites:

        1. Python 2.7+

        2. Python modules installed:

                Jinja2           2.10

                pydot            1.2.4

                pymongo          3.7.1

                Scrapy           1.5.0

                textX            1.7.1

        3. MongoDB database installed (with default settings)

# Item to be scrapped:

For each item there is:

1. Definition of product with properties and css selectors for each property under examples\domain_name\types\type_name.sdt file.

2. Configuration file (.py file) for properties that include more complex manipulation of the tag content under examples\domain_name\types\type_name.py file.

# Usage

Type definition , example:
> Movie (
> title {"div.title_wrapper h1::text"}, 
> year {"div.title_wrapper h1 span#titleYear a::text"},
> rating {"div.ratingValue strong span::text"}, 
> duration{"div.subtext time::text"},
> genre{"div.subtext a::text"},
> release_date {"div.subtext a::text"}, 
> story_line{"div.plot_summary div.summary_text::text"}, 
> director {"div.credit_summary_item a::text"}, 
> writers{"div.credit_summary_item a::text"}, 

Custom py module, which defines work to be performed with extracted tag for each type:
>def Movie_title(content):
>    return content.extract_first().strip()
>
>def Movie_year(content):
>    return content.extract_first().strip()
>
>def Movie_duration(content):
>    return content.extract_first().strip()
>
>def Movie_genre(content):
>   return ", ".join(content.extract()[:-1])
>
>def Movie_release_date(content):
>    return content.extract()[-1].strip()
>
>def Movie_story_line(content):
>   return content.extract_first().strip()
>
>def Movie_writers(content):
>   return content.extract()[1]

Main DSL query is defined under examples\domain_name\type_program.sdq file.

Example (movie_program.sdq):

>find Movie where cast = &#39;Morgan Freeman&#39;

Result:
Scrapy project with Movie as the scraping item and spider_imdb defined with rules defined in previously seen .sdt and .py files.

All the examples are under examples folder. (together with type definition and configuration files)

# How to run:

_\*Code expects all the files regarding the grammar definition to be under dsl/language folder and type definition, configuration and main DSL query in the examples/domain_name folder._

In dsl/generate.py file you define the scraping item and the domain:
> 
    domain = "imdb"
    type = "movie"
>

_\*Currently supported types are: movie, poslanik and most of the products on winwin and gigatron (laptop, mobilni\_telefon, frizider, televizor etc)_

Run generate.py and check the output folder. The scrapy is automatically run.

# Project structure:

- Templates are located at dsl/templates folder
- Generator is in the main dsl folder (with .py extension)
- Language files are in the dsl/language folder.
- Generated Scrapy project is in the dsl/output folder.

# License:

MIT
