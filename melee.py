import pygame
from Ball import Ball

class Melee(Ball):
        def __init__(self, pos, bspeed, direction, owner):
            Ball.__init__(self, "images/LAZER.png", [0,0], pos)
            self.maxSpeed = 20
            if direction == "right": 
                self.speedx = self.maxSpeed
            if direction == "left" :
                self.speedx = -self.maxSpeed

            self.owner = owner
        
        def collidePlayer(self, other):
            if other != self.owner:
                if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                    if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                        self.living = False
                        print "hit"
                
                
        def collideWall (self, width, height):
            if not self.didBounceX: 
                if self.rect.left < 0 or self.rect.right > width:
                    self.living = False
            if not self.didBounceX:
                if self.rect.top < 0 or self.rect.bottom > height:
                    self.living = False
                        
        
