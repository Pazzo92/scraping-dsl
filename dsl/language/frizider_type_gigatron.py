def Frizider_cena(content):
    return content.extract_first().strip().replace(".","")

def Table_name(row_selector):
    return row_selector.css('th::text').extract_first().strip()

def Table_value(row_selector):
    link = row_selector.css('a::text').extract_first()
    if link is not None:
        value = link.strip()
    else:
        value = row_selector.css('td::text').extract_first()
    return value