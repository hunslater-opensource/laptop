import scrapy
import hashlib
import os
from laptop.items import GpuItem
from BeautifulSoup import BeautifulSoup


class GpuSpider(scrapy.Spider):
    name = "gpu"
    #allowed_domains = ["http://www.videocardbenchmark.net"]
    start_urls = ['http://www.videocardbenchmark.net/gpu_list.php']

    def parse(self, response):
        for sel in response.css("table.cpulist a"):
            url = sel.xpath('@href').extract()[0]
            url = 'http://www.videocardbenchmark.net/' + url.replace("video_lookup.php?","gpu.php?")
            yield scrapy.Request(url, self.parse_item)


    def parse_item(self, response):

        item = GpuItem()
        item['link'] = response.url
        item['name'] = response.css('span.cpuname').xpath('text()').extract()[0]

        search = {
            'description': u'Description:',
            #'processzor_modell': u'Videocard Category:',
            'other_name': u'Other names:',
            #'memoria_merete': u'Videocard First Benchmarked:',
            'g3d_mark':u'G3DMark/\$Price:',
            #'memoria_max_seb':u'Overall Rank:',
            #'memoria_foglalat':u'Last Price Change:',

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
