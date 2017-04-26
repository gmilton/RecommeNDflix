#!/usr/bin/env python2.7

import pygame
import datetime
import time
import requests
import sys
import os
from pygame.locals import *

def titlef(horizontal_place, vertical_place):
    title_font = pygame.font.SysFont(None, 52)
    title = title_font.render("R E C O M M E N D F L I X", 1, (255, 255, 255))
    outlinef(horizontal_place, vertical_place)
    background.blit(title, (horizontal_place,vertical_place))

def outlinef(text_horizontal, text_vertical):
    outline_font = pygame.font.Font(None, 52)
    outline = outline_font.render("R E C O M M E N D F L I X", 1, (10, 10, 10))
    background.blit(outline, (text_horizontal - 2,text_vertical - 1)) # 1 up, 1 left
    background.blit(outline, (text_horizontal - 1,text_vertical - 1))
    background.blit(outline, (text_horizontal,text_vertical - 1))
    background.blit(outline, (text_horizontal + 1,text_vertical - 1))
    background.blit(outline, (text_horizontal + 2,text_vertical - 1))
    background.blit(outline, (text_horizontal - 2,text_vertical))
    background.blit(outline, (text_horizontal - 1,text_vertical))
    background.blit(outline, (text_horizontal,text_vertical))
    background.blit(outline, (text_horizontal + 1,text_vertical + 1)) # 1 down, 1 left
    background.blit(outline, (text_horizontal+2,text_vertical+2))
    background.blit(outline, (text_horizontal+3,text_vertical+3))
    background.blit(outline, (text_horizontal+4,text_vertical+4))

def toggle_colors(color_list, index):

    i = 0
    for item in color_list:
        if i != index:
            if item == light_paprika:
                return color_list[index]
        i = i + 1

    if color_list[index] == netflix_red:
        color = light_paprika
    elif color_list[index] == light_paprika:
        color = netflix_red
    return color

def toggle_chosen(old, new, chosen):

    if old == netflix_red and new == light_paprika:
        return True
    elif old == light_paprika and new == netflix_red:
        return False
    else:
        return chosen

# Variables
text_vertical = 100
text_horizontal = 85
run = True
title_screen = True
menu_screen = False
new_screen = False
checkbox_x = 20
checkbox_y = 65
checkbox_size = 10
checkbox_thickness = 2
netflix_red = (185, 9, 11)
light_paprika = (255, 153, 153)
checkbox_color = [netflix_red, netflix_red, netflix_red]
time_color = [netflix_red, netflix_red, netflix_red, netflix_red]
genre_chosen = False
time_chosen = False
WEEKDAY=datetime.datetime.today().weekday()
morning_ff_quotes = []
morning_funny_quotes = []
morning_singalong_quotes = []
afternoon_educational_quotes = []
afternoon_adventure_quotes = []
afternoon_sport_quotes = []
night_scary_quotes = []
night_date_quotes = []
night_world_quotes = []

genre_lists = [[[10751], [16, 35], [10402]], [[36, 99], [10752, 37, 12, 80], [28, 10770]], [[27, 53], [10749, 18], [14, 878, 9648]]]

#print genre_lists[0][0][0];

#---assign each weekday string given weekday integer value---
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

TIMEODAY=time.strftime("%H") #gets the hour of the day

HOUR = int(TIMEODAY)

#---display the correct message based on the current hour---
if HOUR >= 5 and HOUR < 12:
    time_of_day = 'morning'
    time_index = 0
elif HOUR >= 12 and HOUR < 17:
    time_of_day = 'afternoon'
    time_index = 1
else:
    time_of_day = 'night'
    time_index = 2

# Initialize screen
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('RecommeNDflix')

#  background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(netflix_red)

# Display title screen
titlef(text_horizontal, text_vertical) 
start_font = pygame.font.Font('scriptfont.ttf', 40)
start = start_font.render("Start", 1, (200, 200, 200))
background.blit(start, (text_horizontal + 170, text_vertical + 150))

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# Event loop
while run:
    while title_screen:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            title_screen = False
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x > 250 and x < 350:
                if y > 250 and y < 275:
                    menu_screen = True
                    title_screen = False 
    while menu_screen:
	# Background color
        background.fill((185,9,11))
	
	# Message about day/time of day
    	day_font = pygame.font.Font('basicsansserif.ttf', 25)	
    	day_message = day_font.render("You made it to "+str(DAY)+" "+time_of_day+"! Good for you!", 1, (255, 255, 255))
        if (time_of_day == 'morning'):
            # Probably set genre_id number in here
            option1_string = 'Something family-friendly'
            option1_quote = 'Just keep swimming (Finding Nemo, 2003)'
            option2_string = "Something funny and light-hearted"
	    option2_quote ="Gentleman, you can't fight in here! This is the War Room! (Dr. Strangelove, 1964)"
            option3_string = 'Something to sing-along to'
	    option3_quote = 'Tell me about it, stud. (Grease, 1978)'
        if (time_of_day == 'afternoon'):
            option1_string = 'Something educational'
            option1_quote = 'Here at NASA we all pee the same color. (Hidden Figures, 2016)'
            option2_string = 'Something adventurous'
            option2_quote = '...I will look for you, I will find you, and I will kill you. (Taken, 2008)'
            option3_string = 'Something sporty'
            option3_quote = "There's no crying in baseball! (A League of Their Own, 1992)"
        if (time_of_day == 'night'):
            option1_string = 'Something scary'
            option1_quote = 'A census taker one tried to test me. I ate his liver with some fava beans and a nice Chianti. (The Silence of the Lambs, 1991)'
            option2_string = 'Something perfect for date night'
            option2_quote = 'When you realize you want to spend the rest of your life with somebody, you want the rest of your life to start as soon as possible. (When Harry Met Sally, 1989)'
            option3_string = 'Something out of this world'
            option3_quote = "Toto, I've a feeling we're not in Kansas anymore. (The Wizard of Oz, 1939)"

	# Question about what to watch
	genre_font = pygame.font.Font('basicsansserif.ttf', 25)
	genre = genre_font.render("What do you feel like watching?", 1, (255, 255, 255))

	# ------- Genre Options ------------ 
        options_font = pygame.font.SysFont(None, 16)
        quote_font = pygame.font.SysFont(None, 16, False, True)

	# Names for each genre
        option1 = options_font.render(option1_string, 1, (255, 255, 255))
        quote1 = quote_font.render(option1_quote, 1, (255, 255, 255))
        option2 = options_font.render(option2_string, 1, (255, 255, 255))
        quote2 = quote_font.render(option2_quote, 1, (255, 255, 255))
        option3 = options_font.render(option3_string, 1, (255, 255, 255))
        quote3 = quote_font.render(option3_quote, 1, (255, 255, 255))
  
	# Checkboxes for each genre
        pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y, checkbox_size, checkbox_size), checkbox_thickness)
	pygame.draw.rect(background, checkbox_color[0], (checkbox_x+2, checkbox_y+2, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+25, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, checkbox_color[1], (checkbox_x+2, checkbox_y+27, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+50, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, checkbox_color[2], (checkbox_x+2, checkbox_y+52, checkbox_size-4, checkbox_size-4), 0)    	

	# Question about how much time to spend
        time_font = pygame.font.SysFont(None, 30)
        time = time_font.render("How much time do you have?", 1, (255, 255, 255))

	# ---------- Time Options --------------
        times_font = pygame.font.SysFont(None, 16)

	# Ranges of time as options
       	range1 = options_font.render("0 - 1.5 hours", 1, (255, 255, 255))
        range2 = options_font.render("1.5 - 2.5 hours", 1, (255, 255, 255))
        range3 = options_font.render("2.5 - 3 hours", 1, (255, 255, 255))
	range4 = options_font.render("All day, everyday, bruh", 1, (255, 255, 255))
  
	# Checkboxes for each time
        pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+120, checkbox_size, checkbox_size), checkbox_thickness)
	pygame.draw.rect(background, time_color[0], (checkbox_x+2, checkbox_y+120+2, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+140, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, time_color[1], (checkbox_x+2, checkbox_y+142, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+160, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, time_color[2], (checkbox_x+2, checkbox_y+162, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+180, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, time_color[3], (checkbox_x+2, checkbox_y+182, checkbox_size-4, checkbox_size-4), 0)    	

	continue_font = pygame.font.Font(None, 40)
	continue_button = continue_font.render("CONTINUE", 1, (205, 205, 205))

	# Add everything to background
	background.blit(day_message, (10,10))
	background.blit(genre, (10, 35))
	background.blit(option1, (checkbox_x + 15, checkbox_y))
        background.blit(quote1, (checkbox_x + 15, checkbox_y + 10))
	background.blit(option2, (checkbox_x + 15, checkbox_y + 25))
        background.blit(quote2, (checkbox_x + 15, checkbox_y + 35))
	background.blit(option3, (checkbox_x + 15, checkbox_y + 50))
        background.blit(quote3, (checkbox_x + 15, checkbox_y + 60))
	background.blit(time, (10, 150))
        background.blit(range1, (checkbox_x+15, checkbox_y+120))
        background.blit(range2, (checkbox_x + 15, checkbox_y+140))
        background.blit(range3, (checkbox_x + 15, checkbox_y + 160))
        background.blit(range4, (checkbox_x + 15, checkbox_y + 180))
	background.blit(continue_button, (text_horizontal + 120, text_vertical + 250))

	# Add background to screen
	screen.blit(background, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
	if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
	    print x, y, checkbox_x, checkbox_y, checkbox_size
            if x > checkbox_x and x < checkbox_x+checkbox_size:	
                if y > checkbox_y and y < checkbox_y+checkbox_size:
		    old_color = checkbox_color[0]
                    checkbox_color[0] = toggle_colors(checkbox_color, 0)
		    genre_chosen = toggle_chosen(old_color, checkbox_color[0], genre_chosen)
		    if genre_chosen:
                        genre_final = genre_lists[time_index][0]
                if y > checkbox_y+25 and y < checkbox_y+checkbox_size+25:
		    old_color = checkbox_color[1]
                    checkbox_color[1] = toggle_colors(checkbox_color, 1)
		    genre_chosen = toggle_chosen(old_color, checkbox_color[1], genre_chosen)
		    if genre_chosen:
                        genre_final = genre_lists[time_index][1]
                if y > checkbox_y+50 and y < checkbox_y+checkbox_size+50:
		    old_color = checkbox_color[2]
                    checkbox_color[2] = toggle_colors(checkbox_color, 2)
		    genre_chosen = toggle_chosen(old_color, checkbox_color[2], genre_chosen)
		    if genre_chosen:
                        genre_final = genre_lists[time_index][2]
                if y > checkbox_y+120 and y < checkbox_y+checkbox_size+120:
		    old_color = time_color[0]
                    time_color[0] = toggle_colors(time_color, 0)	
		    time_chosen = toggle_chosen(old_color, time_color[0], time_chosen)
		    if time_chosen:
                        time_final = 90;
                if y > checkbox_y+140 and y < checkbox_y+checkbox_size+140:
		    old_color = time_color[1]
                    time_color[1] = toggle_colors(time_color, 1)
		    time_chosen = toggle_chosen(old_color, time_color[1], time_chosen)
		    if time_chosen:
                        time_final = 150;
                if y > checkbox_y+160 and y < checkbox_y+checkbox_size+160:
		    old_color = time_color[2]
                    time_color[2] = toggle_colors(time_color, 2)
		    time_chosen = toggle_chosen(old_color, time_color[2], time_chosen)
		    if time_chosen:
                        time_final = 180;
                if y > checkbox_y+180 and y < checkbox_y+checkbox_size+180:
		    old_color = time_color[3]
                    time_color[3] = toggle_colors(time_color, 3)
		    time_chosen = toggle_chosen(old_color, time_color[3], time_chosen)
		    if time_chosen:
                        time_final = -1;
                print "genre_chose: ", genre_chosen
                print "time_chosen: ", time_chosen
            if x > 200 and x < 360:
                if y > 350 and y < 375:
		    print "genre_chosen: ", genre_chosen
                    print "time_chosen: ", time_chosen
		    if genre_chosen and time_chosen:
                        new_screen = True
                        menu_screen = False 
        if event.type == pygame.QUIT:
            menu_screen = False
            run = False
   
    GENRE_LIST = {}
    genre_key = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    movie_titles = ['','','','','','','','','','','','','','','','','','','','']
   
    url = 'https://api.themoviedb.org/3/genre/movie/list?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US'
    response = requests.get(url)
    data = response.json()

    i = 0
    for genre in data['genres']:
        genre_key[i] = genre['id']
        i = i + 1
#        print genre['id']

    url1 = "https://api.themoviedb.org/3/genre/"
    url2 = "/movies?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US"
    GENRE_LIST = {k: [] for k in genre_key}
    for genre_id in genre_key:
        URL = url1+str(genre_id)+url2
        response2 = requests.get(URL)
        alldata = response2.json()
 #       print alldata
        j = 0
        force_stop = False
        # stores all of the movies associated with a genre in a list
        if not force_stop:
            for movies in alldata['results']:
                movie_titles[j] = movies['original_title']
        #        print movies['original_title']
                # sets the movie list in the dictionary with its key value
                GENRE_LIST[genre_id].append(movie_titles[j])
                j = j + 1
        #        print j
                if j == 20:
                    force_stop = True
                    break

# --------------- Up to here has been making dict ---------------

    omdburl = 'http://www.omdbapi.com/?'

    for key in genre_final:
        value_list = GENRE_LIST[key]
    #    print key
        for a in xrange(len(value_list)):
            mt = value_list[a]
            omdbresponse=requests.get(omdburl+'t='+mt)
            omdbdata=omdbresponse.json()
            if omdbdata['Response'] == 'True':
                runtime = omdbdata['Runtime']
                #print runtime
                runtime = runtime[:-4]
                try:
                    runtime_num = int(runtime)
                    if (runtime_num <= time_final):
                        print mt, runtime_num
                except ValueError:
                    pass



    while new_screen:
      #  for item in genre_final:
      #      print "genre: "+str(item)
      #  print "time: "+str(time_final)
        background.fill((185,9,11))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            new_screen = False
            run = False

#if __name__ == '__main__': main()
