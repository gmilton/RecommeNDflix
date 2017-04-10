#!/usr/bin/env python2.7

#Program: datetime.py
#Author: Katie Lutz
#This program is evidence of executable code that was checked into our repository.
#
#The purpose of this program is to correctly identify the morning, afternoon, or
#night (time of day) that will aid the user in their initial preferences.

import datetime
import time

WEEKDAY=datetime.datetime.today().weekday()

if WEEKDAY==0:
  DAY='Monday'
elif WEEKDAY==1:
  DAY='Tuesday'
elif WEEKDAY==2:
  DAY='Wednesday'
elif WEEKDAY==3:
  DAY='Thursday'
elif WEEKDAY==4:
  DAY='Friday'
elif WEEKDAY==5:
  DAY='Saturday'
else:
  DAY='Sunday'

print 'Today is',DAY
if WEEKDAY > 4:
  print 'It\'s the weekend!'
else:
  print 'Long work week?'

TIMEODAY=time.strftime("%H") #gets the hour of the day

HOUR = int(TIMEODAY)


#print message for appropriate time of day
if HOUR >= 12:
  if HOUR < 18:
    print 'Good afternoon!'
  else:
    print 'Are you looking for something to watch tonight?'
else:
  if HOUR > 6:
    print 'Good morning!'
  else:
    print 'Late night?'

#Hash table research:
#If we have a huge amount of movie and television titles, we need some method
#of accessing each title with a hash algorithm or computation. So, if it
#is the morning/afternoon/night, perhaps there is a way to organize each of 
#the titles by most appropriate for that time of day. The real issue is whether
#or not a movie, such as a comedy, can be placed in both the "morning" and
#"afternoon" sections. We still don't know how hash tables work, but they 
#seem like the most appropriate way of storing the amount of things we're 
#working with. I'm also not quite sure how double hashing or linear probing
#will be appropriate for what we want, too. 

#What needs to happen first and foremost is that although Netflix updates their
#TV and film selections every few days/weeks, it is much easier for us to 
#work with the one set of selections from the very beginning such that the 
#size of the library stays the same and the "spots", or calculated numbers for
#each selection, stay the same throughout the entire project.I think this 
#will save us quite a bit of time in the long run and will hopefully aid us
#in our use of a hash table for the first time.

