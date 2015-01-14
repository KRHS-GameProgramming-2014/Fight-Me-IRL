import pygame, math

class Ball():
        def __init__(self, image, speed = [0,0], pos = [0,0]):
                self.image = pygame.image.load(image)
                self.rect = self.image.get_rect()
                self.speedx = speed[0]
                self.speedy = speed[1]
                self.speed = [self.speedx, self.speedy]
                self.place(pos)
                self.maxSpeed = 10
                self.didBounceX = False
                self.didBounceY = False
                self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
                self.living = True
                
        def place(self, pos):
                self.rect.center = pos
                
        def update(self, width, height):
                self.didBounceX = False
                self.didBounceY = False
                self.speed = [self.speedx, self.speedy]
                self.move()
                self.collideWall(width, height)
                
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
                        if self.rect.bottom > 645:
                                self.speedy = 0
                                self.didBounceY = True
                                #print "hit xWall"
                
        def collideBall(self, other):
                if self != other:
                        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                                        if (self.radius + other.radius) > self.distance(other.rect.center):
                                                if not self.didBounceX:
                                                        self.speedx = -self.speedx
                                                        self.didBouncex = True
                                                if not self.didBounceY:
                                                        self.speedy = -self.speedy
                                                        self.didBounceY = True
                                                        #print "hit Ball"
                                                        
        def collidePlayer(self, other):
                if self != other:
                        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                                        if (self.radius + other.radius) > self.distance(other.rect.center):
                                                self.living = False
        

