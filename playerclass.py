import pygame, math
from projectile import Bullet
from gun import Gun

class Player():
	def __init__(self, image, speed = [0,0], pos = [0,0]):
		self.image = pygame.image.load(image)
		self.rect = self.image.get_rect()
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
		self.maxSpeed = 10
		self.place(pos)
		self.posx = pos[0]
		self.posy = pos[1]
		self.pos = [self.posx, self.posy]
		self.changed = False
		self.didBounceX = False
		self.didBounceY = False
		self.living = True
		self.maxSpeed = 10
		self.pistol = Gun("pistol")
        self.shooting = False
       

	def place(self, pos):
		self.rect.center = pos
		
	def update(self, width, height):
		self.didBounceX = False
		self.didBounceY = False
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
		print self.gun.coolDown
        if self.gun.coolDown > 0:
            if self.gun.coolDown < self.gun.coolDownMax:
                self.gun.coolDown += 1
            else:
                self.gun.coolDown = 0
		
	def move(self):
		self.rect = self.rect.move(self.speed)
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				self.didBounceX = True
				#print "hit xWall"
		if not self.didBounceY:
			if self.rect.bottom > 640:
				self.speedy = 0
				self.didBounceY = False
				#print "hit xWall"
							

		
	def go(self, direction):
		if direction == "down":
			self.facing = "down"
			self.changed = True
			self.speedy = self.maxSpeed
		elif direction == "stop down":
			self.speedy = 0
		if direction == "right":
			self.facing = "right"
			self.changed = True
			self.speedx = self.maxSpeed
		elif direction == "stop right":
			self.speedx = 0
		elif direction == "left":
			self.facing = "left"
			self.changed = True
			self.speedx = -self.maxSpeed
		elif direction == "stop left":
			self.speedx = 0
			
	def fly(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 7

	def shoot(self, command = ""):
		if command == "stop":
			self.shooting = False
		if self.gun.coolDown == 0:
			self.gun.coolDown += 1
			if self.gun.kind == "pistol":
				return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing)]



		
