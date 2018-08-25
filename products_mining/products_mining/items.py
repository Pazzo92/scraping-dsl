# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
#

#Operating system
#Color
#Optics    
#VGA
#SSD    
#Batery    
#Touch screen
#Speakers
#Web camera
#HDMI port
#VGA port
#USB 
#Network card
#Bluetooth
#Card reader 
#Dimensions
#Weight
#

import scrapy

class Laptop(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    screen_size = scrapy.Field()
    screen_type = scrapy.Field()
    screen_resolution = scrapy.Field()
    processor_model = scrapy.Field()
    processor_speed = scrapy.Field()
    catche_memory = scrapy.Field()
    chipset = scrapy.Field()
    ram = scrapy.Field()
    ram_type = scrapy.Field()
    hdd_size = scrapy.Field()
    hdd_type = scrapy.Field()
    graphics_card = scrapy.Field()
    operating_system = scrapy.Field()
    color = scrapy.Field()
    optics = scrapy.Field()
    vga = scrapy.Field()
    batery = scrapy.Field()
    touch_screen = scrapy.Field()
    speakers = scrapy.Field()
    web_camera = scrapy.Field()
    hdmi_port = scrapy.Field()
    usb_2 = scrapy.Field()
    usb_3 = scrapy.Field()
    vga_port = scrapy.Field()
    network_card = scrapy.Field()
    bluetooth = scrapy.Field()
    card_reader = scrapy.Field()
    dimensions = scrapy.Field()
    weight = scrapy.Field()



