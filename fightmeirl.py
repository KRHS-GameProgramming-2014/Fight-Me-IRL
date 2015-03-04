import pygame, sys, random
from Player import Player
from Bullet import Bullet
from melee import Melee

pygame.init()

clock = pygame.time.Clock()

width = 896
height = 700
size = width, height
screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0

run = False

while True:
    bgImage = pygame.image.load("Menu.png").convert()
    bgRect = bgImage.get_rect()

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
    
    bullets = []
    melees = []
    players = [Player([800,593]), Player([100,593])]

    while run and len(players) == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    players[0].go("up")
                if event.key == pygame.K_RIGHT:
                    players[0].go("right")
                if event.key == pygame.K_LEFT:
                    players[0].go("left")
                if event.key == pygame.K_l:
                    bullets += players[0].shoot("fire")
                if event.key == pygame.K_m:
                    melees += players[0].shoot("melee")
                if event.key == pygame.K_w:
                    players[1].go("up")
                if event.key == pygame.K_d:
                    players[1].go("right")
                if event.key == pygame.K_a:
                    players[1].go("left")
                if event.key == pygame.K_SPACE:
                    bullets += players[1].shoot("fire")
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    players[0].go("down")
                if event.key == pygame.K_RIGHT:
                    players[0].go("stop right")
                if event.key == pygame.K_LEFT:
                    players[0].go("stop left")
                if event.key == pygame.K_l:
                    players[0].shoot("stop")
                if event.key == pygame.K_w:
                    players[1].go("down")
                if event.key == pygame.K_d:
                    players[1].go("stop right")
                if event.key == pygame.K_a:
                    players[1].go("stop left")
                if event.key == pygame.K_SPACE:
                    players[1].shoot("stop")
                    
        for player in players:
            player.update(width, height)

        for bullet in bullets:
            bullet.update(width, height)
               
        for bullet in bullets:
            for player in players:
                bullet.collidePlayer(player)
                player.collideBullet(bullet)

        for bullet in bullets:
            if not bullet.living:
                bullets.remove(bullet)
        
        
        for melee in melees:
            melee.update(width, height)
               
        for melee in melees:
            for player in players:
                melee.collidePlayer(player)
                player.collideBullet(melee)

        for melee in melees:
            if not melee.living:
                melees.remove(melee)
        
        for player in players:
            if not player.living:
                print player
                players.remove(player)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bgImage, bgRect)
        for bullet in bullets:
            screen.blit(bullet.image, bullet.rect)
        for melee in melees:
            screen.blit(melee.image, melee.rect)
        for player in players:
            screen.blit(player.image, player.rect)
        pygame.display.flip()
        clock.tick(60)
    run = False

