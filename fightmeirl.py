import pygame, sys, random
from playerclass import Player
from HUD import Text
from HUD import Score
from Button import Button

pygame.init()

clock = pygame.time.Clock()

width = 896
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0
bgI = pygame.image.load("Map.png")
bgR = bgI.get_rect()

screen = pygame.display.set_mode(size)

player1 = Player("p1_walk03.png" ,[10,0],[800,598]) 
player2 = Player("p1_walk03.png",[10,0],[100,598]) 


timer = Score([80, height - 25], "Time: ", 36)
timerWait = 0
timerWaitMax = 6

score = Score([width-80, height-25], "Score: ", 36)

run = False

startButton = Button([width/2, height-300], 
				     "images/Buttons/Start Base.png", 
				     "images/Buttons/Start Clicked.png")

while True:
	while not run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					run = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				startButton.click(event.pos)
			if event.type == pygame.MOUSEBUTTONUP:
				if startButton.release(event.pos):
					run = True
					
		bgColor = r,g,b
		screen.fill(bgColor)
		screen.blit(bgImage, bgRect)
		screen.blit(startButton.image, startButton.rect)
		pygame.display.flip()
		clock.tick(60)
		
	bgImage = pygame.image.load("images/Screens/Main Screen.png").convert()
	bgRect = bgImage.get_rect()
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT: sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("left")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_w or event.key == pygame.K_UP:
					player.go("stop up")
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					player.go("stop right")
				if event.key == pygame.K_s or event.key == pygame.K_DOWN:
					player.go("stop down")
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					player.go("stop left")


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
			if event.key == pygame.K_LEFT:
				player2.go("stop left")
				
	player1.gravity
	player1.gravity


	player1.update(width, height)
	player2.update(width, height)

		


	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgI, bgR)
	screen.blit(player1.image, player1.rect)
	screen.blit(player2.image, player2.rect)
	
	screen.blit(score.image, score.rect)
	screen.blit(timer.image, timer.rect)
	pygame.display.flip()
	clock.tick(60)
