import scrapy
import hashlib
import os
from laptop.items import ArukeresoItem

class ArukeresoSpider(scrapy.Spider):
    name = "arukereso"
    allowed_domains = ["www.arukereso.hu"]
    step = 25
    builder = 'http://www.arukereso.hu/notebook-c3100/f:intel-core-i7-processzor,dedikalt/?start=%s'

    start_urls = [

    ]

    def __init__(self, query=None, *args, **kwargs):
        super(ArukeresoSpider, self).__init__(*args, **kwargs)
        for i in range(0,37):
            self.start_urls.append(self.builder % (i*self.step))
        print self.start_urls


    def parse(self, response):

        md5 = hashlib.md5()
        md5.update(response.url)
        filename = md5.hexdigest() + '.txt'

        #with open(filename, 'wb') as f:
        #    f.write(response.body)

        #for sel in response.css("div.ulined-link > a"):
            #    item = ArukeresoItem()
            #item['link'] = sel.xpath('@href').extract()[0]
            #item['name'] = sel.xpath('text()').extract()[0]
            #yield item

        for sel in response.css("div.list-view a.image"):
            url = sel.xpath('@href').extract()[0]
            yield scrapy.Request(url, self.parse_item)


    def parse_item(self, response):
        md5 = hashlib.md5()
        md5.update(response.url)
        filename = md5.hexdigest() + '.txt'

        #with open(filename, 'wb') as f:
        #    f.write(response.body)

        item = ArukeresoItem()
        item['link'] = response.url
        item['name'] = response.xpath('//title').extract()[0]

        search = {
            'processzor_tipusa': u'Processzor t\xedpusa',
            'processzor_modell': u'Processzor modell',
            'processzor_orajel': u'Processzor \xf3rajel',
            'memoria_merete': u'Mem\xf3ria m\xe9rete',
            'memoria_tipusa':u'Mem\xf3ria t\xedpusa',
            'memoria_max_seb':u'Mem\xf3ria maxim\xe1lis sebess\xe9ge',
            'memoria_foglalat':u'Mem\xf3ria foglalatok sz\xe1ma',
            'memoria_max_meret':u'Mem\xf3ria maxim\xe1lis m\xe9rete',
            'kijelzo_meret': u'Kijelz\u0151 m\xe9rete',
            'kijelzo_felbontas': u'Kijelz\u0151 felbont\xe1sa',
            'videokartya_tipusa': u'Videok\xe1rtya t\xedpusa\xa0',
            'videokartya_model': u'Videok\xe1rtya modell',
            'videokartya_memoria': u'Grafikus mem\xf3ria m\xe9rete',
            'oprend': u'Oper\xe1ci\xf3s rendszer'
        }

        item['price'] = response.css('div.price').xpath('text()').extract()[0]

        for sel in response.css("table.product-properties tr"):
            td = sel.xpath('td/text()').extract()
            #item['description'] = td[0]

            if len(td) == 2:
                #print td
                for key in search:
                    if (search[key] == td[0]):
                        item[key] = td[1]
        yield item
