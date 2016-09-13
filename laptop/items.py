# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArukeresoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    #cpu = scrapy.Field()
    #memory = scrapy.Field()
    #memory_slot = scrapy.Field()
    #vga = scrapy.Field()
    price = scrapy.Field()
    #display = scrapy.Field()
    #description = scrapy.Field()


    processzor_tipusa = scrapy.Field()
    processzor_modell = scrapy.Field()
    processzor_orajel = scrapy.Field()
    memoria_merete = scrapy.Field()
    memoria_tipusa = scrapy.Field()
    memoria_max_seb = scrapy.Field()
    memoria_foglalat = scrapy.Field()
    memoria_max_meret = scrapy.Field()
    kijelzo_meret = scrapy.Field()
    kijelzo_felbontas = scrapy.Field()
    videokartya_tipusa = scrapy.Field()
    videokartya_model = scrapy.Field()
    videokartya_memoria = scrapy.Field()
    oprend = scrapy.Field()

class GpuItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    other_name = scrapy.Field()
    price = scrapy.Field()
    rank = scrapy.Field()
    g3d_mark = scrapy.Field()

class CpuItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    other_name = scrapy.Field()
    price = scrapy.Field()
    rank = scrapy.Field()
    g3d_mark = scrapy.Field()
    clock = scrapy.Field()
    core = scrapy.Field()

