# -*- coding: utf-8 -*-
import scrapy
from  douban.items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['movie.douban.com']
    #start_urls = ['https://movie.douban.com/top250?start=0']
    offset=0
    url='https://movie.douban.com/top250?start='
    start_urls=[url+str(offset)]

    def parse(self, response):
        print(response)
        print(type(response))
        movies=response.xpath('//div[@class="info"]')
        for each in movies:
            # .当前标签下
            #标题
            title=each.xpath('.//span[@class="title"]/text()').extract()[0]
         #   print(title)
            #信息
            info=each.xpath('.//div[@class="bd"]/p[@class=""]/text()').extract()[0]
          #  print(info)
            #评分
            star=each.xpath('.//div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
           # print(star)
            #简介
           # quote=each.xpath('.//div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()[0]
            quote = each.xpath('.//span[@class="inq"]/text()').extract()[0]
            #print(quote)
            item=DoubanItem()
            item['title']=title
            item['info']=info
            item['star']=star
            item['quote']=quote
            yield item
            if self.offset<225:
                self.offset+=25
                yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
