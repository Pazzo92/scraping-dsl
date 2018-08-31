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
        if next_page is not None:
            return [scrapy.Request(next_page, callback=self.parse_links)]
        
    def parse(self,response):
        
        laptop = Laptop()
        laptop['name'] = response.css('h1::text').extract_first()
        laptop['price'] = response.css('div.price-box span.price::text').extract_first().strip()
        
        table = response.css('div.product-panels-content table.data-table')
        for tr in table.css('tr'):
            name = tr.css('th::text').extract_first().strip()
            value = tr.css('td::text').extract_first().strip()
            
            property = self.gigatron_dictionary(name)
            
            if property !='':
                laptop[property] = value
        
        print('laptop')
            
    def winwin_dictionary(self, x):
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
        