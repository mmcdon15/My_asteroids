import pygame
from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    shot_groups=pygame.sprite.Group()
    
    def __init__(self, x, y,shot_group):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation=0
        # python
        for group in getattr(Player, "containers", ()):
            group.add(self)
        self.shot_groups=shot_group
        self.shot_timer=0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    def rotate(self,dt):
        self.rotation+=(PLAYER_TURN_SPEED*dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        tip = self.position + forward * self.radius
        shot = Shot(tip.x,tip.y)
        self.shot_groups.add(shot)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity*=PLAYER_SHOOT_SPEED
        self.shot_timer=PLAYER_SHOOT_COOLDOWN
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
           if self.shot_timer<=0:
            self.shoot()
        self.shot_timer-=dt