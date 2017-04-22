#!/usr/bin/env python2.7
import pygame
import datetime
import time
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


# Initialise screen
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('RecommeNDflix')

#  background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(netflix_red)

# Display title screen
titlef(text_horizontal, text_vertical) 
start_font = pygame.font.Font(None, 40)
start = start_font.render("START", 1, (200, 200, 200))
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
    	day_font = pygame.font.SysFont(None, 30)	
    	day_message = day_font.render("You made it to "+str(DAY)+", bruh, good for you.", 1, (255, 255, 255))

	# Question about what to watch
	genre_font = pygame.font.SysFont(None, 30)
	genre = genre_font.render("What do you feel like watching?", 1, (255, 255, 255))

	# ------- Genre Options ------------ 
        options_font = pygame.font.SysFont(None, 16)

	# Names for each genre
        option1 = options_font.render("Something hella", 1, (255, 255, 255))
        option2 = options_font.render("Something not hella", 1, (255, 255, 255))
        option3 = options_font.render("Surprise me!", 1, (255, 255, 255))
  
	# Checkboxes for each genre
        pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y, checkbox_size, checkbox_size), checkbox_thickness)
	pygame.draw.rect(background, checkbox_color[0], (checkbox_x+2, checkbox_y+2, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+20, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, checkbox_color[1], (checkbox_x+2, checkbox_y+22, checkbox_size-4, checkbox_size-4), 0)    	
	pygame.draw.rect(background, (205,205,205), (checkbox_x, checkbox_y+40, checkbox_size, checkbox_size), checkbox_thickness)    	
	pygame.draw.rect(background, checkbox_color[2], (checkbox_x+2, checkbox_y+42, checkbox_size-4, checkbox_size-4), 0)    	

	# Question about how much time to spend
        time_font = pygame.font.SysFont(None, 30)
        time = time_font.render("How much time would you like to spend watching movies?", 1, (255, 255, 255))

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
	background.blit(option2, (checkbox_x + 15, checkbox_y + 20))
	background.blit(option3, (checkbox_x + 15, checkbox_y + 40))
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
                    checkbox_color[0] = toggle_colors(checkbox_color, 0)
		    print checkbox_color[0]	
                if y > checkbox_y+20 and y < checkbox_y+checkbox_size+20:
                    checkbox_color[1] = toggle_colors(checkbox_color, 1)
                if y > checkbox_y+40 and y < checkbox_y+checkbox_size+40:
                    checkbox_color[2] = toggle_colors(checkbox_color, 2)

                if y > checkbox_y+120 and y < checkbox_y+checkbox_size+120:
                    time_color[0] = toggle_colors(time_color, 0)	
                if y > checkbox_y+140 and y < checkbox_y+checkbox_size+140:
                    time_color[1] = toggle_colors(time_color, 1)
                if y > checkbox_y+160 and y < checkbox_y+checkbox_size+160:
                    time_color[2] = toggle_colors(time_color, 2)
                if y > checkbox_y+180 and y < checkbox_y+checkbox_size+180:
                    time_color[3] = toggle_colors(time_color, 3)
            if x > 200 and x < 360:
                if y > 350 and y < 375:
                    new_screen = True
                    menu_screen = False 
        if event.type == pygame.QUIT:
            menu_screen = False
            run = False
    while new_screen:
        background.fill((185,9,11))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            new_screen = False
            run = False

#if __name__ == '__main__': main()
