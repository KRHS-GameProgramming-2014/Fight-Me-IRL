import pygame
from Ball import Ball

class Bullet(Ball):
    def __init__(self, pos, bspeed, direction, heading2 = None):
		Ball.__init__(self, "Trentsface.png", [0,0], pos)
		if direction == "right" or direction == "up" and "right":
				self.speedx = self.maxSpeed
		if direction == "left" or direction == "up" and "left": 
				self.speedx = -self.maxSpeed
