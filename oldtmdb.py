#!/usr/bin/env python2.7

# Figured out how to take user input and search by genre from dictionary 

import requests
import sys
import json

GENRE_LIST = {}
genre_key = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
movie_titles = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US'
response = requests.get(url)
data = response.json()

i = 0
for genre in data['genres']:
	genre_key[i] = genre['id']
	i = i + 1


url1 = "https://api.themoviedb.org/3/genre/"
url2 = "/movies?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US"
GENRE_LIST = {k: [] for k in genre_key}
for genre_id in genre_key:
	URL = url1+str(genre_id)+url2
	response2 = requests.get(URL)
	alldata = response2.json()
	j = 0
	# stores all of the movies associated with a genre in a list
	for movies in alldata['results']:
		movie_titles[j] = movies['original_title'] 
		# sets the movie list in the dictionary with its key value
		GENRE_LIST[genre_id].append(movie_titles[j])
		j = j + 1

for key in GENRE_LIST.keys():
	value_list = GENRE_LIST[key]
	print key
	for a in xrange(len(value_list)):
		print value_list[a]
	print " "
