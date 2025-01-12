import pygame
import random

from constants import *
from circleshape import CircleShape


class Asteroid (CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)
        
        asteroid1_velocity = self.velocity.rotate(random_angle)
        asteroid2_velocity = self.velocity.rotate(-random_angle) 
        split_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
        
        split_asteroid1 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)
        split_asteroid2 = Asteroid(self.position.x, self.position.y, split_asteroid_radius)


        split_asteroid1.velocity = asteroid1_velocity * 1.2
        split_asteroid2.velocity = asteroid2_velocity * 1.2

