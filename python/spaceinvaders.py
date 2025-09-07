import math
import pygame
import random
SCREEN_WIDTH=800
SCREEN_HEIGHT= 500
PLAYER_START_X=370
PLAYER_START_Y= 380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
background = pygame.image.load("C:/Users/knitt/Downloads/Background image.jpg")
pygame.display.set_caption("Space inavders")

playerImg = pygame.image.load( "C:/Users/knitt/Downloads/—Pngtree—vector free buckle cartoon red_4697052.png")
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("C:/Users/knitt/Downloads/Monster.png"))
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

bulletImg = pygame.image.load("C:/Users/knitt\Downloads/—Pngtree—bullet icon in cartoon style_5151430.png") 
bulletX = 0
bulletY = PLAYER_START_Y   



