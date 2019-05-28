import scrapy
from time import gmtime, strftime


#time stamp
time_stamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

class HMPriceSpider (scrapy.Spider):
	name = "HM_Crawler"

	#take input url as an argument
	def __init__(self, url=None, *args, **kwargs):
		super(HMPriceSpider, self).__init__(*args, **kwargs)
		self.start_urls = [url]


	def parse(self, response):
		#get the main body where all the info stays
		all_info = response.css("main div.inner")	




		#the section containing name and price of the product
		name_price = all_info.css("section.name-price")

		#product name
		name = name_price.css("h1.primary.product-item-headline::text").get().strip()
		#product price
		price = float(response.css("div.primary-row.product-item-price span.price-value::text").get().strip()[1:])

		#time stamp
		time_stamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())

		#size =  all_info.css("div.product-item-buttons button.trigger-button.picker-trigger.js-picker-trigger.small span.value::text").get().strip()

		#warning = all_info.css("div.product-item-buttons button.trigger-button.picker-trigger.js-picker-trigger.small span.info.warning::text").get()
		#if warning is not None:
		#	warning = warning.strip()


		#save name and price into a JSON file, then later will save it to our DB
		return {'url' : self.start_urls,
				'name' : name,
				'price' : price,
				'time_stamp' : time_stamp
				#'size' : size,
				#'warning' : warning
			}



