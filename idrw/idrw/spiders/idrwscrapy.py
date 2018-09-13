# -*- coding: utf-8 -*-
import scrapy


class IdrwscrapySpider(scrapy.Spider):
    name = "idrwscrapy"
    allowed_domains = ["idrw.org"]
    start_urls = (
        'http://www.idrw.org/',
    )

    def parse(self, response):
      
        urls = ('http://www.idrw.org/page/{}'.format(i) for i in range(1,88))
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_page_links)
        

    def parse_page_links(self, response):
        href = response.css('.art-postheader > a::attr(href)').extract()
        urls=[]
        for item in href :
            # yield { 'url' : item }
            urls.append(item)
        for url in urls:
            #yield { 'url' : url }     
            yield scrapy.Request(url, callback=self.parse_info)
        #yield urls
        
    def parse_info(self, response):
        #Extracting the content using css selectors
        title = response.css('.entry-title::text').extract()
        article = response.css('.art-postcontent p').extract()
        images = response.css('.art-postcontent  img::attr(src)').extract()
        yield {'title':title,'article':article,'images':images}
        # #Give the extracted content row wise
        # for item in zip(title,article,images):
        #     #create a dictionary to store the scraped info
        #     yield {
        #         'title' : item[0],
        #         'article' : item[1],#some problem was coming due to zip()
        #         'images' : item[2],
        #     }
