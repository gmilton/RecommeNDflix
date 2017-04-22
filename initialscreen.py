#!/usr/bin/env python2.7
import pygame
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

# Variables
text_vertical = 100
text_horizontal = 85
run = True
title_screen = True
new_screen = False
checkbox_x = 10
checkbox_y = 30
checkbox_size = 10
checkbox_thickness = 2
netflix_red = (185, 9, 11)

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
	    print x, y
            if x > 250 and x < 350:
                if y > 250 and y < 275:
                    new_screen = True
                    title_screen = False 
    while new_screen:
        background.fill((185,9,11))
    	genre_font = pygame.font.SysFont(None, 24)
    	genre = genre_font.render("You made it to Friday, bruh, good for you. What do you feel like watching?", 1, (255, 255, 255))
        time_font = pygame.font.SysFont(None, 52)
        time = time_font.render("Time", 1, (255, 255, 255))
	pygame.draw.rect(background, (0,0,0), (checkbox_x, checkbox_y, checkbox_size, checkbox_size), checkbox_thickness)    	
	background.blit(genre, (10,10))
	background.blit(time, (10, 100))
	screen.blit(background, (0, 0))
        pygame.display.flip()
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            new_screen = False
            run = False

#if __name__ == '__main__': main()
