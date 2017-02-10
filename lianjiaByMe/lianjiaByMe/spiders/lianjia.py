# -*- coding: utf-8 -*-
import scrapy
from ..items import HouseItem,CjHouseItem


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["fs.lianjia.com"]
 #   start_urls = ['http://fs.lianjia.com/chengjiao/']

    def start_requests(self):
        base_url = "http://fs.lianjia.com/chengjiao/{0}/pg{1}"
        place = ["naihai","chancheng","shishan","shunde"]
        for plc in place:
            for p in range(1,20):  # 输入爬取页面的截止页数
                url = base_url.format(plc,p)
                print "adding start urls:"+ url
                yield scrapy.Request(url,dont_filter=True,callback=self.parse)


    def parse(self, response):
        lists = response.css('ul[class="listContent"] li')
        items = []
        for index,list in enumerate(lists):
            item = CjHouseItem()
            item['page_url'] = ''.join(list.css("a[class='img']::attr(href)").extract())
            item['title'] = ''.join(list.css("div[class='title'] a::text").extract())
            item['house_info'] = ''.join(list.css("div[class='houseInfo']::text").extract())
            item['deal_data'] = ''.join(list.css("div[class='dealDate']::text").extract()).replace('.','')
            item['total_price'] = ''.join(list.css("div[class='totalPrice'] span::text").extract())
            item['position_icon'] =  ''.join(list.css("div[class='positionInfo']::text").extract())
            item['unit_price'] = ''.join(list.css("div[class='unitPrice'] span::text").extract())
            item['deal_house_txt'] = ''.join(list.css("div[class='dealHouseInfo'] span::text").extract())
            item['sell_flag'] = 1
            item['house_id'] = str(item['page_url']).split(r'/')[-1].split(r'.')[0]
            item['house_place'] = str(response.url).split(r'/')[-3]
            items.append(item)
        return items

