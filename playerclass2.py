import pygame
from Ball import Ball
from projectile import Bullet
from gun import Gun

class Player(Ball):
    def __init__(self, pos):
        Ball.__init__(self, "p1_walk03.png", [0,0], pos)
        self.upImages = [pygame.image.load("p1_walk03.png"),
                        ]
        self.downImages = [pygame.image.load("p1_walk03.png"),
                          ]
        self.leftImages = [pygame.image.load("p1_walk03.png"),
                           ]
        self.rightImages = [pygame.image.load("p1_walk03.png"),
                            ]
        self.facing = "right"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.pistol = Gun("pistol")
        self.melee = Gun("melee")
        self.gun = self.pistol
        self.shooting = False
        self.life = 0
        
       
    
    def collideBullet(self, other, owner):
        self.owner = owner
        if other != self.owner:
			if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
				if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
					self.life += 1
        if self.life == 5:
            self.living = False
            print "dead"
            
            
    def update(self, width, height):
        Ball.update(self, width, height)
        self.animate()
        self.changed = False

    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
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
            self.speedy = 5
            
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
            
    def shoot(self, command):
        if command == "stop":
            self.shooting = False
        elif command == "fire":
            return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing, self)]
            self.shooting = True
            return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing, self)]
        else:
            return []
            

