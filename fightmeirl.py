import pygame, sys, random
from playerclass2 import Player
from projectile import Bullet

pygame.init()

clock = pygame.time.Clock()

width = 896
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0
bgI = pygame.image.load("Map.png")
bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player1 = Player([800,598]) 
player2 = Player([100,598]) 


#player1 = Player("p1_walk03.png" ,[0,0],[800,598]) 
#player2 = Player("p1_walk03.png",[0,0],[100,598]) 

bullets = []

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player1.go("up")
			if event.key == pygame.K_d:
				player1.go("right")
			if event.key == pygame.K_a:
				player1.go("left")
			if event.key == pygame.K_SPACE:
				bullets += player1.shoot("fire")
			if event.key == pygame.K_UP:
				player2.go("up")
			if event.key == pygame.K_RIGHT:
				player2.go("right")
			if event.key == pygame.K_LEFT:
				player2.go("left")
			if event.key == pygame.K_l:
				bullets += player2.shoot("fire")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player1.go("stop up")
			if event.key == pygame.K_d:
				player1.go("stop right")
			if event.key == pygame.K_a:
				player1.go("stop left")
			if event.key == pygame.K_SPACE:
				player1.shoot("stop")
			if event.key == pygame.K_UP:
				player2.go("stop up")
			if event.key == pygame.K_RIGHT:
				player2.go("stop right")
			if event.key == pygame.K_LEFT:
				player2.go("stop left")
			if event.key == pygame.K_l:
				player2.shoot("stop")
                
				
	player1.update(width, height)	
			
	player2.update(width, height)
	
	for bullet in bullets:
		bullet.update(width, height)
		   
	for bullet in bullets:
		if not bullet.living:
			bullets.remove(bullet)
        
        


	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgI, bgR)
	for bullet in bullets:
		screen.blit(bullet.image, bullet.rect)
	screen.blit(player1.image, player1.rect)
	screen.blit(player2.image, player2.rect)
	pygame.display.flip()
	clock.tick(60)
