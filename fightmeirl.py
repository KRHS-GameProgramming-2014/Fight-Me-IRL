import pygame, sys, random
from playerclass import Player

 

pygame.init()

clock = pygame.time.Clock()

width = 896
height = 700
size = width, height

screen = pygame.display.set_mode(size)

bgColor = r,g,b = 0, 0, 0

bgImage = pygame.image.load("Menu.png").convert()
bgRect = bgImage.get_rect()


player1 = Player("p1_walk03.png" ,[0,0],[800,598]) 
player2 = Player("p1_walk03.png",[0,0],[100,598]) 

#pygame.mixer.music.load("coco.mp3")
#pygame.mixer.music.play(1)

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

    while run:
            bgImage = pygame.image.load("Map.png").convert()
            bgRect = bgImage.get_rect()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player1.fly("up")
                    if event.key == pygame.K_d:
                        player1.go("right")
                    if event.key == pygame.K_a:
                        player1.go("left")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        player1.fly("stop up")
                    if event.key == pygame.K_d:
                        player1.go("stop right")
                    if event.key == pygame.K_a:
                        player1.go("stop left")
				
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player2.fly("up")
                    if event.key == pygame.K_RIGHT:
                        player2.go("right")
                    if event.key == pygame.K_LEFT:
                        player2.go("left")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        player2.fly("stop up")
                    if event.key == pygame.K_RIGHT:
                        player2.go("stop right")
                    if event.key == pygame.K_LEFT:
                        player2.go("stop left")


            player1.update(width, height)
            player2.update(width, height)


            bgColor = r,g,b
            screen.fill(bgColor)
            screen.blit(bgImage, bgRect)
            screen.blit(player1.image, player1.rect)
            screen.blit(player2.image, player2.rect)
            pygame.display.flip()
            clock.tick(60)
