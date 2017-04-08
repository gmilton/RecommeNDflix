#!/usr/bin/env python2.7

import pygame
 
background_colour = (255,64,64)
(width, height) = (600, 400)
 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('RecommeNDflix')
screen.fill(background_colour)
 
pygame.display.flip()
 
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

