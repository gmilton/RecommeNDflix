#!/usr/bin/env python2.7

import requests
import sys
import json

#GENRE_LIST = {}
#def hash(astring, tablesize):
 #   sum = 0
  #  for pos in range(len(astring)):
   #     sum = sum + ord(astring[pos])
#
 #public class HashTable {
 

class HashTable:
    def __init__(self):
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and \
                            self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1) % size

    def get(self,key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)


url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US'
response = requests.get(url)
data = response.json()

H=HashTable()

for genre in data['genres']:
    genre_key = genre['id']
    genre_name = genre['name']
    H[genre_key] = genre_name

for i in H:
    print H[i]


print H.slots
print H.data

