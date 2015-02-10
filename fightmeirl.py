import pygame, sys, random
from Player import Player
from Bullet import Bullet

pygame.init()

clock = pygame.time.Clock()

width = 896
height = 700
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0
bgImage = pygame.image.load("Menu.png").convert()
bgRect = bgImage.get_rect()

player1 = Player([800,593])
player2 = Player([100,593]) 


bullets = []

players = [player1, player2]

run = False

while True:
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = True
                            
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        pygame.display.flip()
        clock.tick(60)
    
    bgImage = pygame.image.load("Map.png").convert()
    bgRect = bgImage.get_rect()
    
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player1.go("up")
                if event.key == pygame.K_RIGHT:
                    player1.go("right")
                if event.key == pygame.K_LEFT:
                    player1.go("left")
                if event.key == pygame.K_l:
                    bullets += player1.shoot("fire")
                if event.key == pygame.K_w:
                    player2.go("up")
                if event.key == pygame.K_d:
                    player2.go("right")
                if event.key == pygame.K_a:
                    player2.go("left")
                if event.key == pygame.K_SPACE:
                    bullets += player2.shoot("fire")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    player1.go("down")
                if event.key == pygame.K_RIGHT:
                    player1.go("stop right")
                if event.key == pygame.K_LEFT:
                    player1.go("stop left")
                if event.key == pygame.K_l:
                    player1.shoot("stop")
                if event.key == pygame.K_w:
                    player2.go("down")
                if event.key == pygame.K_d:
                    player2.go("stop right")
                if event.key == pygame.K_a:
                    player2.go("stop left")
                if event.key == pygame.K_SPACE:
                    player2.shoot("stop")
                    
                    
        player1.update(width, height)
        player2.update(width, height)

        for bullet in bullets:
            bullet.update(width, height)
               
        for bullet in bullets:
            bullet.collidePlayer(player1)
            bullet.collidePlayer(player2)
            player2.collideBullet(bullet)
            player1.collideBullet(bullet)

        for bullet in bullets:
            if not bullet.living:
                bullets.remove(bullet)
        
        for player in players:
            if not player.living:
                print player
                players.remove(player)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for player in players:
            screen.blit(player.image, player.rect)
        pygame.display.flip()
        clock.tick(60)
