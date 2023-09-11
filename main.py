import pygame
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Beginner Flappy Bird")
playerImg = pygame.image.load('rupicola.png')
playerX = 50
playerY = 300
playerY_change = 1
playerX_change = 1
enemyImg = []
enemyX = []
enemyY = []
num_of_enemies = 30

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('alien.png'))
    enemyX.append(250)
    enemyY.append(0)
    enemyX.append(250)
    enemyY.append(50)
    enemyX.append(250)
    enemyY.append(100)
    enemyX.append(250)
    enemyY.append(150)
    enemyX.append(250)
    enemyY.append(300)
    enemyX.append(250)
    enemyY.append(350)
    enemyX.append(250)
    enemyY.append(400)
    enemyX.append(250)
    enemyY.append(450)
    enemyX.append(250)
    enemyY.append(500)
    enemyX.append(250)
    enemyY.append(550)

    # 2nd column
    enemyX.append(425)
    enemyY.append(0)
    enemyX.append(425)
    enemyY.append(50)
    enemyX.append(425)
    enemyY.append(100)
    enemyX.append(425)
    enemyY.append(150)
    enemyX.append(425)
    enemyY.append(200)
    enemyX.append(425)
    enemyY.append(250)
    enemyX.append(425)
    enemyY.append(300)
    enemyX.append(425)
    enemyY.append(450)
    enemyX.append(425)
    enemyY.append(500)
    enemyX.append(425)
    enemyY.append(550)

    # 3nd column
    enemyX.append(600)
    enemyY.append(0)
    enemyX.append(600)
    enemyY.append(50)
    enemyX.append(600)
    enemyY.append(100)
    enemyX.append(600)
    enemyY.append(250)
    enemyX.append(600)
    enemyY.append(300)
    enemyX.append(600)
    enemyY.append(350)
    enemyX.append(600)
    enemyY.append(400)
    enemyX.append(600)
    enemyY.append(450)
    enemyX.append(600)
    enemyY.append(500)
    enemyX.append(600)
    enemyY.append(550)

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def isCollision(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt((math.pow(enemyX - playerX, 2)) + (math.pow(enemyY - playerY, 2)))
    if distance < 30:
        return True
    else:
        return False

running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((100, 100, 111))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                playerY_change = -2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                playerY_change = 1

    playerY += playerY_change
    if playerY <= 0:
        playerY = 300
        playerX = 50
    if playerY >= 565:
        playerY = 300
        playerX = 50

    playerX += playerX_change
    if playerX >= 736:
        playerX = 0

    for i in range(num_of_enemies):
        enemy(enemyX[i], enemyY[i], i)
        collision = isCollision(enemyX[i], enemyY[i], playerX, playerY)

        if collision:
            playerX = 50
            playerY = 300
    player(playerX, playerY)
    pygame.display.update()
