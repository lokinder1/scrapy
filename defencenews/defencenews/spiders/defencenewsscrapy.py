# -*- coding: utf-8 -*-
import scrapy


class DefencenewsscrapySpider(scrapy.Spider):
    name = "defencenewsscrapy"
    allowed_domains = ["defencenews.in"]
    start_urls = (
        'http://www.defencenews.in/article/China%E2%80%99s-2nd-Aircraft-Carrier-heads-for-trials,-India-2nd-carrier-not-far-behind-570260',
    )

    def parse(self, response):
        #Extracting the content using css selectors
        title = response.css('.article-title h2::text').extract()
        article = response.css('.art-discription p').extract()
        images = response.css('.bxslider1 li img::attr(src)').extract()
        
        #Give the extracted content row wise
        for item in zip(title,article,images):
            #create a dictionary to store the scraped info
            scraped_info = {
                'title' : item[0],
                'article' : item[1],
                'images' : item[2],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info
