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
white = (255,255,255)

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Fall down')

BLACK = (0,0,0)
green = (0,255,0)

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 100)

score_font = pygame.font.SysFont(None, 59)

platforms = [] #list to hold the platforms

gravity = 6

ceiling = pygame.image.load('spike.bmp')


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [200, screen_height/2])
    pygame.display.update() #update the screen

def start_message(msg, color, position):
    screen_text = score_font.render(msg, True, color)
    screen.blit(screen_text, [200, position])
    pygame.display.update() #update the screen



class Ball(object):
    def __init__(self):
        self.position = [screen_width/2,100]
        self.img = pygame.image.load('ball.bmp')
        self.speed = 15
        self.radius = 50
        self.rect = pygame.Rect(self.position[0], self.position[1], self.radius, self.radius)

    def move_both_axis(self, dx, dy):
        
        # Move the rect
        self.position[0] += dx
        self.position[1] += dy
        self.rect = pygame.Rect(self.position[0], self.position[1], self.radius, self.radius)
        # If you collide with a wall, move out based on velocity
        for platform in platforms:
            if platform.rect.colliderect(self.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.position[0] = platform.rect.left - self.radius
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.position[0] = platform.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.position[1] = platform.rect.top - self.radius
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.position[1] = platform.rect.bottom

class Platform(object):
    
    def __init__(self, pos):
        platforms.append(self)
        self.img = pygame.image.load('floor.bmp')
        self.rect = pygame.Rect(pos[0], pos[1], 500, 10)
        self.x = pos[0]
        self.y = pos[1]

    def moveaxis(self, dx, dy):
        
        # Move the rect
        self.x += dx
        self.y += dy
        self.rect = pygame.Rect(self.x, self.y, 500, 10)

ball = Ball()

GamePlatList = []


def game_loop():
    timer = 60*3
    start_message("Left and right arrow keys to move, q to quit,", red,screen_height/2)
    start_message ("p to pause for 5 seconds. Don't touch the sides!",red, screen_height/1.5)
    time.sleep(4)
    x = time.time()
    score = 0
    platSpeed = -3.5
    while 1:
        clock.tick(60)
        score += 1
        platSpeed *= 1.0005
        ball.move_both_axis(0, gravity)
        for event in pygame.event.get():
           if event.type == KEYDOWN:
                if event.key == K_q:
                    exit()
                    
        #platform list
        if(timer%(60) == 0):
            
            temprandx = random.randrange(0, 960)
            temprandy = random.randrange(0, 400)

            platform = Platform([temprandx, 720])
            GamePlatList.append(platform)
        if (timer < (60*40)):
            timer += 1.5
        elif(timer >= (60*40) and timer < (60*100)):
            timer += 2
        else:
            timer += 3

        #get all the keys being pressed
        keys = pygame.key.get_pressed()


        if keys[pygame.K_p]:
            message_to_screen("Paused for 5 seconds!", red)
            time.sleep(5)
        if keys[pygame.K_LEFT]:
            ball.move_both_axis(-ball.speed, 0)
        if keys[pygame.K_RIGHT]:
            ball.move_both_axis(ball.speed,0)


        #creates boundaries
        if ball.position[0] > 1280:
            message_to_screen("GAME OVER! Score: {:.0f}".format(score), red)
            time.sleep(3)
            pygame.display.quit()
            pygame.quit()
            exit()
        if ball.position[0] < 0:
            message_to_screen("GAME OVER! Score: {:.0f}".format(score), red)
            time.sleep(3)
            pygame.display.quit()
            pygame.quit()
            exit()
        if ball.position[1] < 75: #hit the top
            message_to_screen("GAME OVER! Score: {:.0f}".format(score), red)
            time.sleep(3)
            pygame.display.quit()
            pygame.quit()
            exit()
        if ball.position[1] > 720: #hit the top
            message_to_screen("GAME OVER! Score: {:.0f}".format(score), red)
            time.sleep(3)
            pygame.display.quit()
            pygame.quit()
            exit()

        for i in GamePlatList:
            i.moveaxis(0, platSpeed)

        screen.fill(BLACK) #fill the screen with black
        #pygame.draw.rect(screen, white, ball.rect)
        screen.blit(ball.img, ball.position) #draw the ball
        p = -5
        while p < screen_width:  
            screen.blit(ceiling, [p,0])
            p = p + 45
        

        for i in GamePlatList:
            screen.blit(i.img, i.rect)

        scoretext = font.render("Score: " + str(score), 1, red)
        screen.blit(scoretext, (5,screen_height-120))

        
        pygame.display.update() #update the screen
#HIGH SCORE IS 2904
game_loop()
