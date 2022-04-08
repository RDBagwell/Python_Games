import math
import pygame
import random

from pygame import mixer

# initialize PyGame
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(30, 150)
enemyX_move_speed = 0.2
enemyX_change = enemyX_move_speed
enemyY_change = 32

# Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bullet_move_speed = 1
bulletX_change = 0
bulletY_change = bullet_move_speed
bullet_state = "ready"

# Score
score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 26, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + (math.pow(enemy_y - bullet_y, 2)))
    if distance < 27:
        return True
    return False


# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Key Binding
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.5
            if event.key == pygame.K_RIGHT:
                playerX_change = .5
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Enemy Movement
    if enemyX <= 0:
        enemyX_change = enemyX_move_speed
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = enemyX_move_speed * -1
        enemyY += enemyY_change
    enemyX += enemyX_change

    # Collision
    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bullet_state = 'ready'
        bulletY = 480
        explosionSound = mixer.Sound('explosion.wav')
        explosionSound.play()
        score += 1
        enemyX = random.randint(0, 735)
        enemyY = random.randint(30, 150)
        print(score)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Player Movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
