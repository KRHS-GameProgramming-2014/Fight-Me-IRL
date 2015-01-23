import pygame
from Ball import Ball

class Bullet(Ball):
		def __init__(self, pos, bspeed, direction,):
			Ball.__init__(self, "Trentsface.png", [0,0], pos)
			if direction == "right" or direction == "up" and "right":
				self.speedx = self.maxSpeed
			if direction == "left" or direction == "up" and "left": 
				self.speedx = -self.maxSpeed
		
		def collidePlayer(self, other):
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					if (self.radius + other.radius) > self.distance(other.rect.center):
						self.living = False
				
				
				
		def collideWall (self, width, height):
			if not self.didBounceX:	
				if self.rect.left < 0 or self.rect.right > width:
					self.living = False
			if not self.didBounceX:
				if self.rect.top < 0 or self.rect.bottom > height:
					self.living = False
						
		
