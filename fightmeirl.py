import pygame, sys, random
from playerclass import Ball


pygame.init()

clock = pygame.time.Clock()

width = 1024 
height = 800
size = width, height

bgColor = r,g,b = 0, 0, 0
bgI = pygame.image.load("")
bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player1 = Player("", [10,0],[760,70]) 
player2 = Player("", [10,0],[760,954]) 


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				player1.go("up")
			if event.key == pygame.K_d:
				player1.go("right")
			if event.key == pygame.K_s:
				player1.go("down")
			if event.key == pygame.K_a:
				player1.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_w:
				player1.go("stop up")
			if event.key == pygame.K_d:
				player1.go("stop right")
			if event.key == pygame.K_s:
				player1.go("stop down")
			if event.key == pygame.K_a:
				player1.go("stop left")
				
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				player2.go("up")
			if event.key == pygame.K_RIGHT:
				player2.go("right")
			if event.key == pygame.K_DOWN:
				player2.go("down")
			if event.key == pygame.K_LEFT:
				player2.go("left")
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				player2.go("stop up")
			if event.key == pygame.K_RIGHT:
				player2.go("stop right")
			if event.key == pygame.K_DOWN:
				player2.go("stop down")
			if event.key == pygame.K_UP:
				player2.go("stop left")
		
	if len(balls) < 10:
		if random.randint(0, .25*60) == 0:
			balls += [Ball("images/Ball/ball.png",
					  [random.randint(0,10), random.randint(0,10)],
					  [random.randint(100, width-100), random.randint(100, height-100)])
					  ]
	player.update(width, height)
	for ball in balls:
		ball.update(width, height)
		
	for bully in balls:
		for victem in balls:
			bully.collideBall(victem)
			bully.collidePlayer(player)
	
	for ball in balls:
		if not ball.living:
			balls.remove(ball)
	
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgI, bgR)
	for ball in balls:
		screen.blit(ball.image, ball.rect)
	screen.blit(player.image, player.rect)
	pygame.display.flip()
	clock.tick(60)
