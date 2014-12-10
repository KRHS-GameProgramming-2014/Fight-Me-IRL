import pygame, sys, random
from playerclass2 import Player


pygame.init()

clock = pygame.time.Clock()

width = 1024 
height = 800
size = width, height

bgColor = r,g,b = 0, 0, 0
bgI = pygame.image.load("Map.png")
bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player1 = Player([10,0],[760,70]) 
player2 = Player([10,0],[760,954]) 


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
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player1.go("stop up")
			if event.key == pygame.K_d:
				player1.go("stop right")
			if event.key == pygame.K_a:
				player1.go("stop left")
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player2.go("up")
			if event.key == pygame.K_RIGHT:
				player2.go("right")
			if event.key == pygame.K_LEFT:
				player2.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player2.go("stop up")
			if event.key == pygame.K_RIGHT:
				player2.go("stop right")
			if event.key == pygame.K_UP:
				player2.go("stop left")
		


	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgI, bgR)
	screen.blit(player1.image, player1.rect)
	screen.blit(player2.image, player2.rect)
	pygame.display.flip()
	clock.tick(60)
