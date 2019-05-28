import scrapy

class QuotesSpider2(scrapy.Spider):

	name = "quotes_saver"

	#since the program will crawl page by page,
	#start url just consists of the first page
	start_urls = [
				'http://quotes.toscrape.com/page/1/',
                ]


    #this function is to save the quote, author and tags into a JSON file           
	def parse (self, response):
	   	#each of the quote will be a Selector Xpath object containing a piece storing a quote, its author and tags
	    for quote in response.css("div.quote"):
	    	yield { 'quote' : quote.css("span.text::text").get(),
	    			'author' : quote.css("small.author::text").get(),
	    			'tags' : quote.css("div.tags a::text").getall()
		   	}

		#next page: page # is in the nav tag  
		
