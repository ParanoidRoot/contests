# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import os

class BaidubaikePipeline(object):

    savePath = os.path.join(os.getcwd(), "data.csv")

    def process_item(self, item, spider):
        with open(self.savePath, "a+", newline='') as outFile :
            csvOutFile = csv.writer(outFile)
            csvOutFile.writerow([item['time'], item['head'], item['content']])
        return item
