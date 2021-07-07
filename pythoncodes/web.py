#!/usr/bin/python3

import requests
import  pandas

data_url='http://winterolympicsmedals.com/medals.csv'
#webdata=requests.get('https://en.wikipedia.org/wiki/DevOps')
webdata=requests.get(data_url)

if webdata.status_code == 200 :
	print("Successful...")
	# reading data using csv 
	mydata=pandas.read_csv(data_url)
	print(mydata.head(10))
	print(mydata.head(10)['Year'])

elif webdata.status_code == 404 :
	print("URL Not Found ")

else : 
	print("I need to check this...")



