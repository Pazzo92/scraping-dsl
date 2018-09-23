def Mobilni_telefon_cena(content):
    return content.extract_first().strip()[:-5].replace(".","")

def Table_name(row_selector):
    return row_selector.css('th::text').extract_first().strip()

def Table_value(row_selector):
    return row_selector.css('td::text').extract_first()