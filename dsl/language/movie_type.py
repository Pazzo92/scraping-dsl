def Movie_title(content):
    return content.extract_first().strip()

def Movie_year(content):
    return content.extract_first().strip()

def Movie_duration(content):
    return content.extract_first().strip()

def Movie_genre(content):
    return ", ".join(content.extract()[:-1])

def Movie_release_date(content):
    return content.extract()[-1].strip()

def Movie_story_line(content):
    return content.extract_first().strip()

def Movie_writers(content):
    return content.extract()[1]

def Movie_cast(content):
    cast = []
    for tr in content.css('tr'):
        actor = tr.css('td a::text').extract_first() 
        if actor is not None:
            cast.append(actor.strip())
    return ', '.join(cast)