import pygame, math


class Player():
	def __init__(self, speed = [0,0], pos = [760,70]):
		self.upImages = [pygame.image.load("Game/Player1/p1_walk03.png"),
						 pygame.image.load("Game/Player1/p1_walk03.png"),
						 pygame.image.load("Game/Player1/p1_walk03.png")]
		self.downImages = [pygame.image.load("Game/Player1/p1_walk03.png"),
						   pygame.image.load("Game/Player1/p1_walk03.png"),
						   pygame.image.load("Game/Player1/p1_walk03.png")]
		self.leftImages = [pygame.image.load("Game/Player1/p1_walk03.png"),
						   pygame.image.load("Game/Player1/p1_walk03.png"),
						   pygame.image.load("Game/Player1/p1_walk03.png")]
		self.rightImages = [pygame.image.load("Game/Player1/p1_walk03.png"),
						    pygame.image.load("Game/Player1/p1_walk03.png"),
						    pygame.image.load("Game/Player1/p1_walk03.png")]
		self.facing = "up"
		self.changed = False
		self.didBounceX = False
		self.didBounceY = False
		self.living = True
		self.speedx = speed[0]
		self.speedy = speed[1]
		self.speed = [self.speedx, self.speedy]
		self.place(pos)
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
			
	def update(self, width, height):
		self.didBounceX = False
		self.didBounceY = False
		self.speed = [self.speedx, self.speedy]
		self.move()
		self.collideWall(width, height)
		Ball.update(self, width, height)
		self.animate()
		self.facingChanged = False
		
	def place(self, pos):
		self.rect.center = pos
	
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
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				self.didBounceY = True
				#print "hit xWall"
	
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 1
		else:
			self.waitCount = 0
			self.facingChanged = True
			if self.frame < self.maxFrame:
				self.frame += 1
			else:
				self.frame = 0
		
		if self.changed:	
			if self.facing == "up":
				self.images = self.upImages
			elif self.facing == "down":
				self.images = self.downImages
			elif self.facing == "right":
				self.images = self.rightImages
			elif self.facing == "left":
				self.images = self.leftImages
			
			self.image = self.images[self.frame]
	
	def go(self, direction):
		if direction == "up":
			self.facing = "up"
			self.changed = True
			self.speedy = -self.maxSpeed
		elif direction == "stop up":
			self.speedy = 0
		elif direction == "down":
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
			
	def distance(self, pt):
		x1 = self.rect.center[0]
		y1 = self.rect.center[1]
		x2 = pt[0]
		y2 = pt[1]
		return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
