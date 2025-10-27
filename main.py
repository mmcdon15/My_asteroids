import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt =0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player1=Player((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen,(0,0,0))
        for spr in drawable:
            spr.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player1):
                print("Game Over!")
                sys.exit()
        #screen.fill((0, 0, 0))
        pygame.display.flip()
        dt=clock.tick(60)/1000
if __name__ == "__main__":
    main()
