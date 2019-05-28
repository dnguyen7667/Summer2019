from bs4 import BeautifulSoup as bs
import requests

import re
import time
import schedule
from datetime import datetime


#Need User Agent to access the webpage
#user agent = "identity" of our browser

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
headers = {"User-Agent": USER_AGENT}
current_price = 0

def job():
	url= "https://www2.hm.com/en_us/productpage.0601238003.html"
	page = requests.get(url, headers= headers)

	#print(page.status_code)
	#code 200= the page is present


	#without user_agent, we got cde 403 : page forbidden- apparently HM webpage won't let us get in without specifying USER_AGENT
	#Convert a Response into bs4 object
	#convert a Response into bytes then bytes into soup object
	page_content = page.content
	soup= bs(page_content, 'lxml')
	#manually examine to see where the prices are at
	#which tag is the price in?

	#find the container containing the price
	price_container = soup.find_all("div", {"class": "primary-row product-item-price"})

	#actual price is within span, it appears with $ at first so we trim the "$" and convert to float
	price = float(price_container[0].span.text.strip()[1:])
	#yay so I got the price

	current_price = price
	print ("Price = ", current_price, str(datetime.now()))


schedule.every(5).seconds.do(job)


i = 10

while 1:
	schedule.run_pending()
	time.sleep(1)
	
