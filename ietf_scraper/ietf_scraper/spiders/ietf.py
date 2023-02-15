# -*- coding: utf-8 -*-
import scrapy
import w3lib.html

class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # CSS
        # title = response.css('span.title::text').get()
        # XPath
        # title = response.xpath('//span[@class="title"]/text()').get()
        # return python dictionary

        # XPath tag selectors
        # /html/body/div/h1
        # //h1
        # //div/h1
        # //div//h1
        # //span[@class="title"]/text()
        # //span[@class="title"]/@id

        # author
        author = response.xpath('//span[@class="author-name"]/text()').get()
        title = response.xpath('//span[@class="title"]/text()').get()
        date = response.xpath('//span[@class="date"]/text()').get()
        subtitle = response.xpath('//span[@class="subheading"]/text()').getall()
        text = w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        description = response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get()

        return {'title': title, 'author': author, 'date': date, 'desciption': description, 'subtitle': subtitle, 'text': text}
