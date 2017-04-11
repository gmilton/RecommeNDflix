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
    outline_font = pygame.font.Font(None, 52)
    outline = outline_font.render("RecommeNDflix", 1, (10, 10, 10))
    title_font = pygame.font.Font(None, 52)
    title = title_font.render("RecommeNDflix", 1, (255, 255, 255))
    background.blit(outline, (165,99)) # 1 up, 1 left
    background.blit(outline, (166,99))
    background.blit(outline, (167,99))
    background.blit(outline, (168,99))
    background.blit(outline, (169,99))
    #background.blit(outline, (170,99)) # 1 down, 1 left
    #background.blit(outline, (171,100)) 
    #background.blit(outline, (172,101))
    #background.blit(outline, (173,102))
    #background.blit(outline, (163,100)) # 1 up, 1 left
    #background.blit(outline, (164,100))
    background.blit(outline, (165,100))
    background.blit(outline, (166,100))
    background.blit(outline, (167,100))
    background.blit(outline, (168,101)) # 1 down, 1 left
    background.blit(outline, (169,102))
    background.blit(outline, (170,103))
    background.blit(outline, (171,104))    
    #background.blit(outline, (169,102))
    #background.blit(outline, (174,103))
    #background.blit(outline, (175,104))
    #background.blit(outline, (176,105))
    #background.blit(outline, (173,108))
    #background.blit(outline, (174,109))
    background.blit(title, (167,100))
    start_font = pygame.font.Font(None, 52)
    start = start_font.render("RecommeNDflix", 1, (255, 255, 255))
    #textpos = text.get_rect()
    #textpos.centerx = background.get_rect().centerx
    #textpos.centery = background.get_rect().centery
    #background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
