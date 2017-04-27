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

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('LOGO')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
done = False
NDImg = pygame.image.load('NotreDameFightingIrish.svg.png')
NDImg = pygame.transform.scale(NDImg,(100, 100))
def logo(x,y):
    gameDisplay.blit(NDImg, (x,y))

x =  (150)
y = (150)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    gameDisplay.fill(white)
    logo(x,y)

        
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
