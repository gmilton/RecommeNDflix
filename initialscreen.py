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
    text_horizontal = 97; 
    outline_font = pygame.font.Font(None, 52)
#<<<<<<< HEAD
#    outline = outline_font.render("RecommeNDflix", 1, (10, 10, 10))
#    title_font = pygame.font.Font(None, 52)
#    title = title_font.render("RecommeNDflix", 1, (255, 255, 255))
#    background.blit(outline, (165,99)) # 1 up, 1 left
#    background.blit(outline, (166,99))
#    background.blit(outline, (167,99))
#    background.blit(outline, (168,99))
#    background.blit(outline, (169,99))
#=======
    outline = outline_font.render("R E C O M M E N D F L I X", 1, (10, 10, 10))
    font = pygame.font.Font(None, 52)
    text = font.render("R E C O M M E N D F L I X", 1, (255, 255, 255))
    background.blit(outline, (text_horizontal - 2,text_vertical - 1)) # 1 up, 1 left
    background.blit(outline, (text_horizontal - 1,text_vertical - 1))
    background.blit(outline, (text_horizontal,text_vertical - 1))
    background.blit(outline, (text_horizontal + 1,text_vertical - 1))
    background.blit(outline, (text_horizontal + 2,text_vertical - 1))
#>>>>>>> e39f46c106ddc2a476cbec6bfd59a901470d937c
    #background.blit(outline, (170,99)) # 1 down, 1 left
    #background.blit(outline, (171,100)) 
    #background.blit(outline, (172,101))
    #background.blit(outline, (173,102))
    #background.blit(outline, (163,100)) # 1 up, 1 left
    #background.blit(outline, (164,100))
    background.blit(outline, (text_horizontal - 2,text_vertical))
    background.blit(outline, (text_horizontal - 1,text_vertical))
    background.blit(outline, (text_horizontal,text_vertical))
    background.blit(outline, (text_horizontal + 1,text_vertical + 1)) # 1 down, 1 left
    background.blit(outline, (text_horizontal+2,text_vertical+2))
    background.blit(outline, (text_horizontal+3,text_vertical+3))
    background.blit(outline, (text_horizontal+4,text_vertical+4))    
    #background.blit(outline, (169,102))
    #background.blit(outline, (174,103))
    #background.blit(outline, (175,104))
    #background.blit(outline, (176,105))
    #background.blit(outline, (173,108))
    #background.blit(outline, (174,109))
#<<<<<<< HEAD
#    background.blit(title, (167,100))
#    start_font = pygame.font.Font(None, 52)
#    start = start_font.render("RecommeNDflix", 1, (255, 255, 255))
#=======
    background.blit(text, (text_horizontal,text_vertical))
#>>>>>>> e39f46c106ddc2a476cbec6bfd59a901470d937c
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
