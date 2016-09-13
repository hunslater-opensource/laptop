import scrapy
import hashlib
import os
from laptop.items import CpuItem
from BeautifulSoup import BeautifulSoup


class CpuSpider(scrapy.Spider):
    name = "cpu"
    #allowed_domains = ["http://www.cpubenchmark.net"]
    start_urls = ['http://www.cpubenchmark.net/cpu_list.php']
    def parse(self, response):
        for sel in response.css("table.cpulist a"):
            url = sel.xpath('@href').extract()[0]
            url = 'http://www.cpubenchmark.net/' + url.replace("cpu_lookup.php?","cpu.php?")
            yield scrapy.Request(url, self.parse_item)


    def parse_item(self, response):

        item = CpuItem()
        item['link'] = response.url
        item['name'] = response.css('span.cpuname').xpath('text()').extract()[0]

        search = {
            'description': u'Description:',
            'other_name': u'Other names:',
            'g3d_mark':u'G3DMark/\$Price:',
            'clock':u'Clockspeed:',
            'core':u'No of Cores:'
        }

        rank = u'Samples:'

        i = 0
        for sel in response.css("table.desc tr")[1].xpath('td'):
            text = sel.extract()
            textSplit = text.split(u'<span style="font-weight: bold;">')
            for ii in textSplit:
                cleantext = BeautifulSoup(ii).text
                for si in search:
                    if (cleantext.find(search[si]) != -1 ):
                        item[si] = cleantext.replace(search[si],"")
                if (cleantext.find(rank) != -1):
                    item['rank'] = cleantext.split(rank)[0]

            i = i+1
        yield item
