#this is to save the html page

import scrapy

class QuotesSpider(scrapy.Spider):

    name = "quotes"


    #this function is to provide the webpages 
    #and return the html content as the form of scrapy.response through scrapy.Request() function
    def start_requests(self):
        start_urls = [
                    'http://quotes.toscrape.com/page/1/',
                    'http://quotes.toscrape.com/page/2/']

        for url in start_urls:
            yield scrapy.Request(url, callback = self.parse)



    #this function is to get what we want to be done scrapping
    #taking response returned from start_requests() function above        
    def parse(self, response):
        #page number is the second from the last element
        page = response.url.split('/')[-2]
        filename = "quotes-%s.html" % page

        with open(filename, 'wb') as f:
            f.write(response.body)

        self.log("Save file %s" % filename)

