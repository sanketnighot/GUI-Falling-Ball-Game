import pygame
import time
import sys
import random
import math
import os
import getopt
import pygame
from socket import *
from pygame.locals import *
screen_width = 1280
screen_height = 720
red = (255,0,0)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Fall down')

BLACK = (0,0,0)
green = (0,255,0)


clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)

score_font = pygame.font.SysFont(None, 25)

keys = pygame.key.get_pressed()

def message_to_screen(msg, color):
	screen_text = font.render(msg, True, color)
	screen.blit(screen_text, [450, screen_height/2])
	pygame.display.update() #update the screen

def score_to_screen(time, color):
	screen_text = score_font.render("Score:" + time, True, color)
	screen.blit(screen_text, [1280, screen_height/2])
	pygame.display.update() #update the screen

def timerScore():
	for i in range(0, 99999999): # 3.1709791983764584961 years
		score_to_screen(str(i), green)
		time.sleep(1)


class Ball(pygame.sprite.Sprite):
	def __init__(self, ball):
		ballImg = pygame.image.load("ball.png")
		ballPosition = [0,0]
		speed = 10
	

	 #depending on what key the user presses, update ball x and y position accordingly
	def move(self):
		if keys[pygame.K_UP]:
			ballPosition[1] -= speed # this will eventually be deleted
        if keys[pygame.K_DOWN]:
            ballPosition[1] += speed
        if keys[pygame.K_LEFT]:
            ballPosition[0] -= speed
        if keys[pygame.K_RIGHT]:
            ballPosition[0] += speed
	
     #creates boundaries
	def checkBounds(self):
		if ballPosition[0] > 1280:
			message_to_screen("GAME OVER", red)
			exit()
        if ballPosition[0] < 0:
        	message_to_screen("GAME OVER", red)
        	exit()
        if ballPosition[1] < 0: #hit the top
        	message_to_screen("GAME OVER!", red)
        	time.sleep(1)
        	exit()

def game_loop():
    while 1:
    	clock.tick(60)
        for event in pygame.event.get():
           if event.type == KEYDOWN:
				if event.key == K_q:
					exit()

        #get all the keys being pressed
       

        #timerScore() FIGURE OUT WHERE TO PUT THIS SO IT WORKS
        
        ball.move()

        ball.checkBounds()
        #deal with game over screen later
        '''	
        	for event in pygame.event.get(): 
        		if event.type == KEYDOWN:
        			if event.key == K_q:
        				exit()
        			elif event.key == K_p:
        				game_loop()
        		#time.sleep(1)
        	
        	#exit()
        	'''
        screen.fill(BLACK) #fill the screen with black
        screen.blit(ballImg, ballPosition) #draw the ball
        pygame.display.update() #update the screen


game_loop()
