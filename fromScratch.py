import pygame
import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
pygame.init()

white = (255,255,255)
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fall down')


running = True

while running:
	for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_q:
					running = False

	pygame.display.update()				
	pygame.draw.rect(screen, white, [0,500,10,10])
