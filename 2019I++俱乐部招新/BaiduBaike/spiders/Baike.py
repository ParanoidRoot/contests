# -*- coding: utf-8 -*-
import scrapy
from BaiduBaike.items import BaidubaikeItem
import time

class BaikeSpider(scrapy.Spider):
    name = 'Baike'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E5%8D%A1%E5%86%85%E5%9F%BA%C2%B7%E6%A2%85%E9%9A%86%E5%A4%A7%E5%AD%A6']

    totalNumber = None

    @classmethod
    def initCls(cls) :
        cls.totalNumber = 0

    @classmethod
    def calculate(cls) :
        cls.totalNumber += 1

    @classmethod
    def isEnd(cls) :
        return cls.totalNumber >= 100

    def parse(self, response):

        if not BaikeSpider.totalNumber :
            BaikeSpider.initCls()

        h1 = response.xpath('//dd[@class = "lemmaWgt-lemmaTitle-title"]/h1/text()').extract()
        h2 = response.xpath('//dd[@class = "lemmaWgt-lemmaTitle-title"]/h2/text()').extract()
        head = h1 + h2
        head = "".join(head)

        allTexts = response.xpath(
            '//div[contains(@class, "lemma-summary")]/div[contains(@class, "para")]//text()'
        ).extract()
        content = "".join([text for text in allTexts if "[" not in text])
        content = content.replace("\n", "").replace("\xa0", "")
        # print("content = ", repr(content))

        currentTime = time.strftime("%Y-%m-%d %X")

        item = BaidubaikeItem()
        item["time"] = currentTime
        item["head"] = head
        item["content"] = content

        yield item

        BaikeSpider.calculate()
        print(BaikeSpider.totalNumber)
        if BaikeSpider.isEnd() :
            return

        hrefs = response.xpath(
            '//div[@class = "main-content"]//a[contains(@href, "/item")]/@href'
        ).extract()

        for index, value in enumerate(hrefs) :
            if BaikeSpider.isEnd() :
                return
            newUrl = "https://baike.baidu.com" + value
            yield scrapy.Request(
                newUrl,
                callback=self.parse
            )













