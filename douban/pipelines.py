# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  pymongo
from scrapy.conf import  settings

from douban.items import DoubanItem
class DoubanPipeline(object):
    def process_item(self, item, spider):
        data = dict(item)
        self.post.insert(data)
        return item
        # if isinstance(item,DoubanItem):
        #     content=item.__str__()
        #    # with open("Douban.txt","a",encoding='utf8') as f:
        #         # f.write(content)
        #         # f.write('\n')
        #         # f.flush()
        #     data=dict(content)#转成字典
        #     self.post.insert(data)
        # return item
    def __init__(self):
        host=settings['MONGODB_HOST']
        port=settings['MONGODB_PORT']
        dbname=settings['MONGODB_DBNAME']
        sheetname=settings['MONGODB_SHEETNAME']

        client =pymongo.MongoClient(host=host,port=port)
        #指定存放的数据库
        mydb=client[dbname]
        #存放的表名
        self.post=mydb[sheetname]

