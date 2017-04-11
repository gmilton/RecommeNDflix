#!/usr/bin/env python2.7
import pygame
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('RecommeNDflix')

    #  background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((185, 9, 11))

    # Display title screen
    text_vertical = 100;
    text_horizontal = 85; 
    outline_font = pygame.font.Font(None, 52)
    outline = outline_font.render("R E C O M M E N D F L I X", 1, (10, 10, 10))
    title_font = pygame.font.Font(None, 52)
    title = title_font.render("R E C O M M E N D F L I X", 1, (255, 255, 255))
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
    background.blit(title, (text_horizontal,text_vertical))
    start_font = pygame.font.Font(None, 40)
    start = start_font.render("Start", 1, (200, 200, 200))
    background.blit(start, (text_horizontal + 175, text_vertical + 150))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    run = True
    title_screen = True
    new_screen = False
    while run:
        while title_screen:
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                title_screen = False
		run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
		new_screen = True
                title_screen = False 
        while new_screen:
            background.fill((185,9,11))
	    screen.blit(background, (0, 0))
            pygame.display.flip()
            event = pygame.event.poll()
            if event.type == pygame.QUIT:
                new_screen = False
                run = False
            #screen.blit(background, (0, 0))
    return

if __name__ == '__main__': main()
