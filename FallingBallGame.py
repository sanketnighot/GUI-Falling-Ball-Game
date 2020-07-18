import pygame
from pygame.locals import *
import random
from pygame import mixer

pygame.init()

mixer.music.load('bg.mp3')
mixer.music.play(-1)

# Create the Screen
screen = pygame.display.set_mode((450, 700))

# Title and Icon and Background
pygame.display.set_caption("Falling Ball by @SanketNighot")

ballX = 225
ballY = 15
ballX_change = 0
ballY_change = 3
WHITE = (255, 255, 255)

supportX = 0
supportY = 650
supportX_change = 1

supportY_change = 2
isupportY_change = 2

isupportX = 300
isupportY = 1100
isupportX_change = 1

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)
overfont = pygame.font.Font('Cyberpunks.ttf', 40)

textX = 10
textY = 10


def game_over_text():
    over_txt = overfont.render("GAME OVER", True, (255, 255, 255))
    over_txt2 = overfont.render(f"Your Score is {score_value}", True, (255, 255, 255))
    screen.blit(over_txt2, (90, 360))
    screen.blit(over_txt, (132, 300))


def showScore(x, y):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def Ball(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 15)


def Support(x, y):
    pygame.draw.rect(screen, WHITE, Rect(x, y, 150, 30))


running = True
while running:
    pygame.time.delay(10)
    screen.fill((0, 0, 0))
    showScore(textX, textY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key Strokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX_change = -3

            if event.key == pygame.K_RIGHT:
                ballX_change = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                ballX_change = 0

    if 0 < score_value < 100:
        supportY_change = 2
        isupportY_change = 2
    elif 100 < score_value < 200:
        supportY_change = 3
        isupportY_change = 3
    elif 200 < score_value < 300:
        supportY_change = 4
        isupportY_change = 4
    elif 300 < score_value < 400:
        supportY_change = 5
        isupportY_change = 5

    if 0 < ballY < 700:
        ballX += ballX_change
        ballY += ballY_change
        if ballX in range(0, 155) and ballY in range(supportY - 35, supportY):
            ballY = supportY - 16

        Ball(ballX, ballY)
        if ballX < 15:
            ballX = 17
        if ballX > 435:
            ballX = 435

        supportY -= supportY_change
        if supportY < -36:
            supportY = random.randint(650, 710)

        isupportY -= isupportY_change
        if isupportY < -36:
            isupportY = random.randint(650, 710)

        if supportY == 30 or isupportY == 30:
            score_value += 10

        if ballX in range(300, 450) and ballY in range(isupportY - 35, isupportY):
            ballY = isupportY - 18

        Support(supportX, supportY)
        Support(isupportX, isupportY)
    else:
        game_over_text()

    pygame.display.update()
