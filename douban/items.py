# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #标题
    title=scrapy.Field()
    #信息
    info=scrapy.Field()
    #评分
    star=scrapy.Field()
    #简介
    quote=scrapy.Field()
    #转成str 序列化
    def __str__(self):
        return "title:{} info:{} star:{} quote:{}".format(self["title"],self["info"],self["star"],self["quote"])

