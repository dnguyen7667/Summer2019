import scrapy



class ASOSPriceSpider(scrapy.Spider):
	name = "ASOS_Crawler"

	
	def parse(self, response):
		return 100
