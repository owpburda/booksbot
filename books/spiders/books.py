# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'https://televizory-dvb-t2-hevc.heureka.cz',
    ]

    def parse(self, response):
        self.log('Just visited' + response.url)
