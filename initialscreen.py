#!/usr/bin/env python2.7

import pygame
import datetime
import time
import requests
import sys
import os
import json
import random
from pygame.locals import *

# ---------------- FUNCTIONS ------------------

# Function to draw title
def titlef(horizontal_place, vertical_place):
    title_font = pygame.font.SysFont(None, 52)
    title = title_font.render("R E C O M M E N D F L I X", 1, (255, 255, 255))
    outlinef(horizontal_place, vertical_place)
    background.blit(title, (horizontal_place,vertical_place))

# Function to give title outline
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

# Switches color of checkbox when clicked
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

# Returns true if checkbox clicked
def toggle_chosen(old, new, chosen):
    if old == netflix_red and new == light_paprika:
        return True
    elif old == light_paprika and new == netflix_red:
        return False
    else:
        return chosen

# ---------- VARIABLES -----------------
#def main:

# Integers
text_vertical = 100
text_horizontal = 85
checkbox_x = 20
checkbox_y = 70
checkbox_size = 10
checkbox_thickness = 2

# Booleans
run = True
title_screen = True
menu_screen = False
results_screen = False
genre_chosen = False
time_chosen = False

# Colors
netflix_red = (185, 9, 11)
light_paprika = (255, 153, 153)

# Lists
checkbox_color = [netflix_red, netflix_red, netflix_red]
time_color = [netflix_red, netflix_red, netflix_red, netflix_red]
genre_lists = [[[10751], [16, 35], [10402]], [[36, 99], [10752, 37, 12, 80], [28, 10770]], [[27, 53], [10749, 18], [14, 878, 9648]]]
time_final = [0,0]
chosen_movies = []

# Datetime info
WEEKDAY=datetime.datetime.today().weekday()

# Dictionaries
final_dict = {}

# ------------- WEEKDAY INFORMATION -------------------

# Assign each weekday string given weekday integer value 
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

# Return hour of day as int
TIMEODAY=time.strftime("%H")
HOUR = int(TIMEODAY)

# Set time of day and index to use for lists 
if HOUR >= 5 and HOUR < 12:
    time_of_day = 'morning'
    time_index = 0
elif HOUR >= 12 and HOUR < 17:
    time_of_day = 'afternoon'
    time_index = 1
else:
    time_of_day = 'night'
    time_index = 2

# ---------------- SCREEN --------------------

# Initialize screen
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('RecommeNDflix')

# Background
#bg = pygame.image.load("Pattern_1.png")

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(netflix_red)


# Display title screen
titlef(text_horizontal, text_vertical) 
start_font = pygame.font.Font('scriptfont.ttf', 40)
start = start_font.render("(Start)", 1, (200, 200, 200))
background.blit(start, (text_horizontal + 160, text_vertical + 150))

# Blit everything to the screen
screen.blit(background, (0, 0))
pygame.display.flip()

# ----------------- PROGRAM -------------------------

# Event loop
# Runs until quit has been clicked
while run:
    # ----- Title Screen ----
    while title_screen:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            title_screen = False
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x > 250 and x < 355:
                if y > 250 and y < 310:
                    menu_screen = True
                    title_screen = False 
    # ---- User Interactive/Menu Screen ----
    while menu_screen:
	# Background color
        background.fill((185,9,11))
	
	# Message about day/time of day
    	day_font = pygame.font.Font('basicsansserif.ttf', 30)	
    	day_message = day_font.render("You made it to "+str(DAY)+" "+time_of_day+"! Good for you!", 1, (255, 255, 255))

        # Strings to display by genre checkboxes
        if (time_of_day == 'morning'):
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
            option1_quote = 'Whenever feasible, one should always try to eat the rude. (The Silence of the Lambs, 1991)'
            option2_string = 'Something perfect for date night'
            option2_quote = "I'll have what she's having. (When Harry Met Sally, 1989)"
            option3_string = 'Something out of this world'
            option3_quote = "Toto, I've a feeling we're not in Kansas anymore. (The Wizard of Oz, 1939)"

	# Question about Genre
	genre_font = pygame.font.Font('basicsansserif.ttf', 30)
	genre = genre_font.render("What do you feel like watching?", 1, (255, 255, 255))

	# --------- Genre Options ------------ 
        options_font = pygame.font.Font('sans.ttf', 14)
        quote_font = pygame.font.Font('sansitalic.ttf', 13)

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
        time_font = pygame.font.Font("basicsansserif.ttf", 30)
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

        # Continue Button
	continue_font = pygame.font.Font("scriptfont.ttf", 40)
	continue_button = continue_font.render("Continue", 1, (205, 205, 205))

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
	background.blit(continue_button, (text_horizontal + 140, text_vertical + 200))

	# Add background to screen
	screen.blit(background, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()

        # Check for Events
	if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if x > checkbox_x and x < checkbox_x+checkbox_size:	
                # First Genre Checkbox Checked
                if y > checkbox_y and y < checkbox_y+checkbox_size:
		    old_color = checkbox_color[0]
                    checkbox_color[0] = toggle_colors(checkbox_color, 0)
		    genre_chosen = toggle_chosen(old_color, checkbox_color[0], genre_chosen)
		    if genre_chosen:
                        genre_final = genre_lists[time_index][0]
                # Second Genre Checkbox Checked
                if y > checkbox_y+25 and y < checkbox_y+checkbox_size+25:
		    old_color = checkbox_color[1]
                    checkbox_color[1] = toggle_colors(checkbox_color, 1)
		    genre_chosen = toggle_chosen(old_color, checkbox_color[1], genre_chosen)
		    if genre_chosen:
                        genre_final = genre_lists[time_index][1]
                # Third Genre Checkbox Checked
                if y > checkbox_y+50 and y < checkbox_y+checkbox_size+50:
		    old_color = checkbox_color[2]
                    checkbox_color[2] = toggle_colors(checkbox_color, 2)
		    genre_chosen = toggle_chosen(old_color, checkbox_color[2], genre_chosen)
		    if genre_chosen:
                        genre_final = genre_lists[time_index][2]
                # First Time Checkbox Checked
                if y > checkbox_y+120 and y < checkbox_y+checkbox_size+120:
		    old_color = time_color[0]
                    time_color[0] = toggle_colors(time_color, 0)	
		    time_chosen = toggle_chosen(old_color, time_color[0], time_chosen)
		    if time_chosen:
                        time_final[0] = 0
                        time_final[1] = 90
                # Second Time Checkbox Checked 
                if y > checkbox_y+140 and y < checkbox_y+checkbox_size+140:
		    old_color = time_color[1]
                    time_color[1] = toggle_colors(time_color, 1)
		    time_chosen = toggle_chosen(old_color, time_color[1], time_chosen)
		    if time_chosen:
                        time_final[0] = 90
                        time_final[1] = 150
                # Third Time Checkbox Checked
                if y > checkbox_y+160 and y < checkbox_y+checkbox_size+160:
		    old_color = time_color[2]
                    time_color[2] = toggle_colors(time_color, 2)
		    time_chosen = toggle_chosen(old_color, time_color[2], time_chosen)
		    if time_chosen:
                        time_final[0] = 150
                        time_final[1] = 180
                # Fourth Time Checkbox Checked
                if y > checkbox_y+180 and y < checkbox_y+checkbox_size+180:
		    old_color = time_color[3]
                    time_color[3] = toggle_colors(time_color, 3)
		    time_chosen = toggle_chosen(old_color, time_color[3], time_chosen)
		    if time_chosen:
                        time_final[0] = 0
                        time_final[1] = -1;
            # Continue Button Clicked
            if x > 220 and x < 360:
                if y > 300 and y < 360:
		    if genre_chosen and time_chosen:
                        results_screen = True
                        menu_screen = False 
        if event.type == pygame.QUIT:
            menu_screen = False
            run = False

    # --------- Get Movies From Dictionary Based On Genre And Time Range Chosen ------------
    if results_screen: 

        # ------------------------ DICTIONARY CREATION ---------------------------------
  
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
            
        url1 = "https://api.themoviedb.org/3/genre/"
        url2 = "/movies?api_key=2fa8f55ea7e61c1512068ada4ad5b25a&language=en-US"
        GENRE_LIST = {k: [] for k in genre_key}
        for genre_id in genre_key:
            URL = url1+str(genre_id)+url2
            response2 = requests.get(URL)
            alldata = response2.json()
            j = 0
            force_stop = False
            # Stores all of the movies associated with a genre in a list
            if not force_stop:
                for movies in alldata['results']:
                    movie_titles[j] = movies['original_title']
                    # Sets the value for each key
                    GENRE_LIST[genre_id].append(movie_titles[j])
                    j = j + 1
                    if j == 20:
                        force_stop = True
                        break

        # --------------- END OF DICTIONARY CREATION ---------------

        # Cross reference movies narrows down by genre with times
        omdburl = 'http://www.omdbapi.com/?'

        for key in genre_final:
            value_list = GENRE_LIST[key]
            for a in xrange(len(value_list)):
                mt = value_list[a]
                omdbresponse=requests.get(omdburl+'t='+mt)
                omdbdata=omdbresponse.json()
                if omdbdata['Response'] == 'True':
                    runtime = omdbdata['Runtime']
                    runtime = runtime[:-4]
                    try:
                        runtime_num = int(runtime)
                        if time_final[1] != -1:
                            if runtime_num <= time_final[1]:
                                final_dict[mt] = runtime_num
                        else:
                            final_dict[mt] = runtime_num
                    except ValueError:
                        pass

        # Randomize list
	keys = final_dict.keys()
        random.shuffle(keys)

        # Choose movies to display and keep within time range
        main_count = 0
        while True:
            count = main_count
            pick_time = 0
            time_tally = final_dict[keys[count]]
            chosen_movies.append(keys[count])
            count = count + 1
            # Keep movies below maximum
            if time_final[1] != -1:
                while time_tally < time_final[1] and count < len(final_dict):
                    pick_time = final_dict[keys[count]]
                    if time_tally + pick_time <= time_final[1]:
                        time_tally = time_tally + pick_time
                        chosen_movies.append(keys[count])
                    count = count + 1
            else:
                while count < len(final_dict) and count < 7:
                    pick_time = final_dict[keys[count]]
                    time_tally = time_tally + pick_time
                    chosen_movies.append(keys[count])
                    count = count + 1 
            # Exit if above minimum time limit
            if time_tally > time_final[0]:
                break
            # Reset movies chosen otherwise and iterate to begin with next movie
            else:
                main_count = main_count + 1
                del chosen_movies[:]
         
    # ---------- Results Screen ------------
    while results_screen:
        background.fill((185,9,11))
        xpos = 80
        ypos = 100
        
        # Display title
        titlef(80, 60)
        
        # Display movie titles
        for item in chosen_movies:      
            results_font = pygame.font.Font("basicsansserif.ttf", 18)
            results = results_font.render(item+" ("+str(final_dict[item])+" minutes)", 1, (255, 255, 255))
            background.blit(results, (xpos, ypos))
            ypos = ypos + 30
   
        # Display total time
        tally_font = pygame.font.Font("funfont1.ttf", 30)
        tally = tally_font.render("Total time: "+str(time_tally)+" minutes", 1, (0, 0, 0))
        background.blit(tally, (80, ypos))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            results_screen = False
            run = False

#if __name__ == '__main__': main()
