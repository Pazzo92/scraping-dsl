def Poslanik_ime(content):
    return content.extract_first().strip().split(' ')[0].lower().capitalize()

def Poslanik_prezime(content):
    return content.extract_first().strip().split(' ')[2].lower().capitalize()

def Poslanik_biografija(content):
    strbio = ''
    for line in content.extract():
        strbio += line.strip()
    return strbio

def Table_name(row_selector):
    return row_selector.css('label::text').extract_first().strip().replace(':','')

def Table_value(row_selector):
    link = row_selector.css('a::text').extract_first()
    if link is not None:
        value = link.strip()
    else:
        value = row_selector.css('::text').extract()
        for line in value:
            value = line.strip()
    return value