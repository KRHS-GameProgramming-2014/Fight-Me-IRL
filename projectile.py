import pygame
from Ball import Ball

class Bullet(Ball):
        def __init__(self, pos, bspeed, heading, heading2 = None):
                Player.__init__(self, "Trentsface.png", [0,0], pos)
                if direction == "right":
                        self.speedx = -self.maxSpeed
                if direction == "left": 
                        self.speedx = -self.maxSpeed

        def collideZombie(self, other):
                if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                        if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                                if (self.radius + other.radius) > self.distance(other.rect.center):
                                        self.living = False
        
        def collideWall(self, width, height):
                if not self.didBounceX:
                        #print "trying to hit Wall"
                        if self.rect.left < 0 or self.rect.right > width:
                                self.living = False
                if not self.didBounceY:
                        if self.rect.top < 0 or self.rect.bottom > height:
                                self.living = False
