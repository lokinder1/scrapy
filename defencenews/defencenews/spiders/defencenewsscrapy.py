# -*- coding: utf-8 -*-
import scrapy


class DefencenewsscrapySpider(scrapy.Spider):
    name = "defencenewsscrapy"
    allowed_domains = ["defencenews.in"]
    start_urls = (
        'http://www.defencenews.in/',
    )

    def parse(self, response):
        href = response.css('.News-blk > .news_title > a::attr(href)').extract()
        urls=[]
        for item in href :
            #yield { 'url' : item }
             urls.append(item)
        for url in urls:
            # yield { 'url' : url }     
            yield scrapy.Request(url, callback=self.parse_info)
        # yield urls
        
    def parse_info(self, response):
        #Extracting the content using css selectors
        title = response.css('.article-title h2::text').extract()
        article = response.css('.art-discription p').extract()
        images = response.css('.bxslider1 li img::attr(src)').extract()
        
        #Give the extracted content row wise
        for item in zip(title,article,images):
            #create a dictionary to store the scraped info
            yield {
                'title' : item[0],
                'article' : item[1],
                'images' : item[2],
            }

   
