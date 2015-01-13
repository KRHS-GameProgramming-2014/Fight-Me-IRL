import pygame
from Ball import Ball

class Bullet(Ball):
    def __init__(self, pos, bspeed, direction, heading2 = None):
		Ball.__init__(self, "Trentsface.png", [0,0], pos)
		if direction == "right":
				self.speedx = -self.maxSpeed
		if direction == "left": 
				self.speedx = -self.maxSpeed
