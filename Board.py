import random

import pygame
from pygame.rect import Rect

from Constants import Colors
from Obstacle import Obstacle


class Board:
    def __init__(self):
        self.rect = Rect(0, 400, 720, 80)
        self.obstacles = []

        self.points = 0

        self.time_elapsed_since_last_action = 0
        self.delay_for_next = random.randrange(800, 2500)
        self.clock = pygame.time.Clock()

    def draw(self, surface):
        pygame.draw.rect(surface, Colors.RED.value, self.rect)

        for o in self.obstacles:
            o.draw(surface)

    def tick(self):
        dt = self.clock.tick()
        self.time_elapsed_since_last_action += dt
        if self.time_elapsed_since_last_action > self.delay_for_next:
            self.time_elapsed_since_last_action = 0
            self.delay_for_next = random.randrange(800, 2500)
            self.generate_obstacles()

        for o in self.obstacles:
            if o.can_be_remove():
                self.obstacles.remove(o)
                self.points += 1
            else:
                o.tick()

    def generate_obstacles(self):
        self.obstacles.append(Obstacle(700, 380, 2))

    def reset(self):
        self.points = 0
        self.obstacles = []
        self.time_elapsed_since_last_action = 0
        self.delay_for_next = random.randrange(800, 2500)

