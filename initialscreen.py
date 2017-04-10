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
    font = pygame.font.Font(None, 36)
    text = font.render("RecommeNDflix", 1, (10, 10, 10))
    background.blit(text, (200,100))
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
