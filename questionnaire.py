#!/usr/bin/env python2.7

# Program: questionnaire.py 
# Author: Roann Yanes
# This program acts as evidence of executable code that I have checked into our repository.
# This program asks the user a series of questions to figure out the user's preferences to create a personalized Netflix watching schedule for the user. 
# It is basically a questionnaire. The program outputs the user's responses to the terminal in a nicely formatted way.
# To run the program, just enter './questionnaire.py' at the command line.  

import os
import re
import sys

import requests


# Global variables (These are the questions that we will ask the user to create a customized Netflix schedule.)

QUESTION1 = 'Please enter a name or a nickname: '
QUESTION2 = 'What movie/TV show genre do you prefer? '
QUESTION3 = 'Please rank the following in order of importance (least to most) to you. Please enter each ranking on a separate line:  ~ Mood     ~ Genre     ~ Time Constraint'
QUESTION4 = 'What emotion are you feeling right now? '
QUESTION5 = 'How many hours a day would you like to watch Netflix? '
QUESTION6 = 'What days would you like to watch Netflix?  Please enter each day on a separate line, and enter a blank line when done: '

# These are the variables that we will store the user's responses in.

NAME = ' '
GENRE = ' '
RANK = []
MOOD = ' '
HOURS = ' '
DAYS = []

# These are the variables to change the text outputted to the terminal.

OKBLUE = '\033[94m'

# Main execution (This is a survey to figure out the user's preferences to create a customized Netflix schedule.)

NAME = raw_input(QUESTION1) # asks the user for a name
print ' '

GENRE = raw_input(QUESTION2) # asks the user for favorite genre
print ' '

print QUESTION3 # asks the user to rank three options in order of importance
for i in xrange(3): # range starts from 0 and ends at 3
	rank = raw_input() # stores the input
    	RANK.append(rank) # adds input to the list
print ' '

MOOD = raw_input(QUESTION4) # asks the user what mood the user is in
print ' '

HOURS = raw_input(QUESTION5) # asks the user how many hours a day the user would like to watch Netflix
print ' '

days = raw_input(QUESTION6) # asks the user what days the user would like to watch Netflix
while(len(days) > 0):
	DAYS.append(days.strip()) # adds input to the list
	days = raw_input('Please enter another day or press enter to signify that you are done: ') # stores the input
print ' '

print 'Thank you! Here is a summary of your responses: ' # prints a summary of the user's responses in a nicely formatted way
print("""\
  _   _ ______ _______ ______ _      _______   __   _____  _____ _    _ ______ _____  _    _ _      ______    _____ _____  ______       _______ ____  _____  
 | \ | |  ____|__   __|  ____| |    |_   _\ \ / /  / ____|/ ____| |  | |  ____|  __ \| |  | | |    |  ____|  / ____|  __ \|  ____|   /\|__   __/ __ \|  __ \ 
 |  \| | |__     | |  | |__  | |      | |  \ V /  | (___ | |    | |__| | |__  | |  | | |  | | |    | |__    | |    | |__) | |__     /  \  | | | |  | | |__) |
 | . ` |  __|    | |  |  __| | |      | |   > <    \___ \| |    |  __  |  __| | |  | | |  | | |    |  __|   | |    |  _  /|  __|   / /\ \ | | | |  | |  _  / 
 | |\  | |____   | |  | |    | |____ _| |_ / . \   ____) | |____| |  | | |____| |__| | |__| | |____| |____  | |____| | \ \| |____ / ____ \| | | |__| | | \ \ 
 |_| \_|______|  |_|  |_|    |______|_____/_/ \_\ |_____/ \_____|_|  |_|______|_____/ \____/|______|______|  \_____|_|  \_\______/_/    \_\_|  \____/|_|  \_\
                                                                                                                                                             
                                                                                                                                                             """)
print OKBLUE + "		Hello, {}!".format(NAME)
print OKBLUE + "		You prefer {} movies/TV shows.".format(GENRE)
print OKBLUE + "		Your order of preference is:"
print '					' , ', '.join(RANK)
print OKBLUE + "		You are currently {}.".format(MOOD)
print OKBLUE + "		You would like to watch {} hours of Netflix a day.".format(HOURS)
print OKBLUE + "		You would like to watch Netflix on:"
print '					' , ', '.join(DAYS)
