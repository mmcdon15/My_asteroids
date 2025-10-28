import pygame
from circleshape import *
from constants import *
import random

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

    def split(self):
        self.kill()
        if self.radius <=ASTEROID_MIN_RADIUS:
            return
        else:
           new_angle= random.uniform(20,50)
           child_radius = self.radius-ASTEROID_MIN_RADIUS
           asteroid1=Asteroid(self.position.x,self.position.y,child_radius)
           asteroid1.velocity=self.velocity.rotate(new_angle)
           asteroid1.velocity*=1.2
           asteroid2=Asteroid(self.position.x,self.position.y,child_radius)
           asteroid2.velocity=self.velocity.rotate(-new_angle)
           asteroid2.velocity*=1.2
           print(self.velocity.length())