#!/usr/bin/env python2.7

import requests
import os 
import sys
import json
import re
GENRE = 35

LIMIT = 5
def usage(status=0):
    print '''Usage: {} . [ -g GENRE -n NUMITEMS ]
        -g      GENRE       Genre of the show you want (default: Comedy)
	-n 	LIMIT	    Limit the number of items you want
    '''.format(os.path.basename(sys.argv[0]))
    sys.exit(status)


args = sys.argv[1:]
while len(args) and args[0].startswith('-') and len(args[0]) > 1:
    arg = args.pop(0)
    if arg == '-h':
        usage(0)
    elif arg == '-g':
	GENRE = args.pop(0)	
    elif arg == '-n':
        LIMIT = int(args.pop(0))
    else: 
	usage(1)


url1 = "https://api.themoviedb.org/3/genre/"
url2 = "/movies?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US"
URL = url1+str(GENRE)+url2

response = requests.get(URL)

alldata = response.json()

i = 1
for title in alldata['results']:
    if (i <= LIMIT): 
        print title['title'], title['id']
       # print title['id']
        i = i + 1

# vim: set sts=4 sw=4 ts=8 expandtab ft=cpp
