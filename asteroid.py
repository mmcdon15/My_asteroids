import pygame
from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,x,radius)
        self.rotation = 0
        for group in getattr(Asteroid, "containers", ()):
            group.add(self)
    
    def draw(self,screen):
        pygame.draw.circle(screen, "white",(self.position),2)
    
    def update(self,dt):
        self.position+=(self.velocity*dt)