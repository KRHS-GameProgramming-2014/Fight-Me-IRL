import pygame

class Gun():
        def __init__(self, kind):
                self.coolDown = 0
                if kind == "pistol":
                        self.kind = kind
                        self.gunSpeed = 1000
                        self.ammo = None
                        self.coolDownMax = 1000
                        self.shootcount = 0
                if kind == "melee":
                        self.kind = kind
                        self.gunSpeed = 1
                        self.ammo = None
                        self.coolDownMax = 1000
                        self.shootcount = -1000000
