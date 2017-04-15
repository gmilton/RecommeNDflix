#!/usr/bin/env python2.7

# Figured out how to take user input and search by genre from dictionary 

import requests
import sys
import json

GENRE_LIST = {}

url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US'
response = requests.get(url)
data = response.json()

#for title in data[

for genre in data['genres']:
	genre_key = genre['id']
	genre_name = genre['name']
	GENRE_LIST[genre_key] = genre_name

for i in GENRE_LIST:
	print GENRE_LIST[i]

genre_search = raw_input('Enter a genre to search by: ')

for j in GENRE_LIST:
	if genre_search == GENRE_LIST[j]:
		GENRE = j

url1 = "https://api.themoviedb.org/3/genre/"
url2 = "/movies?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US"
URL = url1+str(GENRE)+url2

response2 = requests.get(URL)

alldata = response2.json()

for title in alldata['results']:
        print title['title']
