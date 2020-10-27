import urllib3
import requests
from bs4 import BeautifulSoup as bs
import json
import time


class Autoru_parser:

	def parse(x):

		end_list = []
		price_list = []

		mass_mark = {'vesta' : 'vaz/', 'a4' : 'audi/','focus' : 'ford/','camry' : 'toyota/'}

		page_url =  'https://auto.ru/sankt-peterburg/cars/'+ mass_mark[x] + x + '/used/'
		but_getter = requests.get(page_url)
		but_html = bs(but_getter.content,'html.parser')
		page_range = but_html.select('span.Button__text')

		page_value = page_range[-4]
		page_ = int(page_value.text)

		

		car_massive = {
		'focus' : 'https://auto.ru/sankt-peterburg/cars/ford/focus/used/?page=',
		'vesta' : 'https://auto.ru/sankt-peterburg/cars/vaz/vesta/used/?page=',
		'a4' : 'https://auto.ru/sankt-peterburg/cars/audi/a4/used/?page=',
		'camry' : 'https://auto.ru/sankt-peterburg/cars/toyota/camry/used/?page='}

		
		for i in range(1,page_+1):

			print(i)
			pager = str(i)
			url = car_massive[x] + pager + '&output_type=list'
			getter = requests.get(url)
			html = bs(getter.content,'html.parser')
			
			content_name = html.select('.ListingItemTitle-module__container')
			content_price = html.select('.ListingItemPrice-module__content')
			content_year = html.select('.ListingItem-module__year')

			double = list(zip(content_name,content_price,content_year))

			for it in double:
				
				temp_list = []
				name = it[0].text
				price = it[1].text
				
				for ite in price:
					if ite.isdigit() == True:
						temp_list.append(ite)
				end_price = "".join(temp_list)
				
				year = it[2].text
				price_list.append(name)
				price_list.append(end_price)
				price_list.append(int(year[0:4]))

		return price_list

