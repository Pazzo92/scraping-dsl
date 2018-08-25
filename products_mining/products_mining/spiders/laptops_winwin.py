import scrapy
from scrapy.http import Request
from scrapy.contrib.loader import ItemLoader
import products_mining.items
from products_mining.items import Laptop

class WinwinLaptopSpider(scrapy.Spider):
    name = "winwin_laptops"
    
    def start_requests(self):
        #url = 'https://www.winwin.rs/laptop-i-tablet-racunari/laptop-notebook-racunari.html'
        url = 'https://www.winwin.rs/laptop-i-tablet-racunari/laptop-notebook-racunari.html?manufacturer=53700'
        return [scrapy.Request(url, callback=self.parse_links)]
    
    def parse_links(self,response):
        links = response.xpath("//*/h2[@class='product-name']/a/@href").extract()
        for link in links:
            return [scrapy.Request(link)]   
        
        next_page = response.xpath("//*/a[@class='next i-next']/@href").extract_first()
        print('da')
        if next_page is not None:
            return [scrapy.Request(next_page, callback=self.parse_links)]
        
    def parse(self,response):
        
        laptop = Laptop()
        laptop['name'] = response.css('h1::text').extract_first()
        laptop['price'] = response.css('div.price-item.currency-item h5::text').extract_first().strip()
        
        table = response.css('div.main.clearfix table.product-specs')
        for tr in table.css('tr'):
            name = tr.css('th::text').extract_first()
            if name == 'GrafiÄ�ka karta':
                value = tr.css('a::text').extract_first().strip()
            elif name == 'HDD1':
                value = str(tr.css('td::text').extract_first()).split(':')[1]
            elif name == 'Ekran':
                value = tr.css('td::text').extract()[1].split(':')[1].strip()
            elif name == 'Procesor':
                value = tr.css('a::text').extract_first()
            else:
                value = tr.css('td::text').extract_first().strip()
            
            property = self.gigatron_dictionary(name)
            if property == 'processor_model':
                laptop['processor_speed'] = tr.css('td::text').extract()[0].split(':')[1].strip()
                laptop['catche_memory'] = tr.css('td::text').extract()[1].split(':')[1].strip()
            elif property == 'screen_resolution':
                laptop['screen_type'] = tr.css('td::text').extract()[0].strip()
            
            if property !='':
                laptop[property] = value
        
        print('laptop')
            
    def gigatron_dictionary(self, x):
        return {
        'RAM memorija': 'ram',
        'Dijagonala ekrana': 'screen_size',
        'Ekran': 'screen_resolution',
        'Ekran osetljiv na dodir' : 'touch_screen',
        'Procesor' : 'processor_model',
        'ÄŒipset' : 'chipset',
        'GrafiÄ�ka karta': 'graphics_card',
        'HDD1' : 'hdd_size',
        'Tip HDD1' : 'hdd_type',
        'OptiÄ�ki ureÄ‘aj' : 'optics',
        'ZvuÄ�nici' : 'speakers' ,
        'Web kamera' : 'web_camera',
        'HDMI' : 'hdmi_port',
        'VGA' : 'vga_port',
        'USB 2.0' : 'usb_2',
        'USB 3.0' : 'usb_3',
        'MreÅ¾na kartica' : 'network_card',
        'Bluetooth' : 'bluetooth',
        'ÄŒitaÄ� kartica' : 'card_reader',
        'Baterija' : 'batery',
        'Operativni sistem' : 'operating_system',
        'Boja': 'color',
        'Dimenzije (Å  x D x V)' : 'dimensions',
        'TeÅ¾ina (kg)' : 'weight',
        'Memorija' : 'ram_type'
        }.get(x, '')   
        
        
        