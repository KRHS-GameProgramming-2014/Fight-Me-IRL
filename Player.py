import pygame
from Ball import Ball
from Bullet import Bullet
from melee import Melee
from gun import Gun

class Player(Ball):
    def __init__(self, pos, facing):
        if facing == "right":
            self.side = "left"
        else:
            self.side = "right"
        Ball.__init__(self, "images/p1_walk01.png", [0,0], pos)
        self.upImages = [pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),
                         pygame.image.load("Game/Player1/p1_jump.png"),]
        self.downImages = [pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png")]
        self.leftImages = [pygame.image.load("Game/Player1/p1_walk01L.png"),
                           pygame.image.load("Game/Player1/p1_walk02L.png"),
                           pygame.image.load("Game/Player1/p1_walk03L.png"),
                           pygame.image.load("Game/Player1/p1_walk04L.png"),
                           pygame.image.load("Game/Player1/p1_walk05L.png"),
                           pygame.image.load("Game/Player1/p1_walk06L.png"),
                           pygame.image.load("Game/Player1/p1_walk07L.png"),
                           pygame.image.load("Game/Player1/p1_walk08L.png"),
                           pygame.image.load("Game/Player1/p1_walk09L.png"),
                           pygame.image.load("Game/Player1/p1_walk10L.png"),
                           pygame.image.load("Game/Player1/p1_walk11L.png")]
        self.rightImages = [pygame.image.load("Game/Player1/p1_walk01.png"),
                           pygame.image.load("Game/Player1/p1_walk02.png"),
                           pygame.image.load("Game/Player1/p1_walk03.png"),
                           pygame.image.load("Game/Player1/p1_walk04.png"),
                           pygame.image.load("Game/Player1/p1_walk05.png"),
                           pygame.image.load("Game/Player1/p1_walk06.png"),
                           pygame.image.load("Game/Player1/p1_walk07.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk09.png"),
                           pygame.image.load("Game/Player1/p1_walk10.png"),
                           pygame.image.load("Game/Player1/p1_walk11.png")]
        self.stopImages = [pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png"),
                           pygame.image.load("Game/Player1/p1_walk08.png")]

        self.facing = facing
        self.changed = False
        self.images = self.rightImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = self.rect.center)
        self.pistol = Gun("pistol")
        self.fist = Gun("melee")
        self.gun = self.pistol
        self.shooting = False
        self.living = True
    
    def collideBullet(self, other):
        if other.owner != self:
            if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    self.living = False
                    print "dead"  
            
    def update(self, width, height):
        Ball.update(self, width, height)
        self.animate()
        self.changed = False


    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 5
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
            elif self.facing == "stop":
                self.images = self.stopImages
            self.image = self.images[self.frame]

                
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxSpeed
        elif direction == "down":
            self.facing = "down"
            self.changed = True
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
        if self.facing != "up":
            if self.facing != "down":
                if command == "fire":
                    return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing,self)]
                    self.shooting = True
                if command == "melee":
                    return[Melee(self.rect.center, self.gun.gunSpeed, self.facing,self)]
                    self.shooting = True
        return []
