import pygame
from pygame.rect import Rect

from Constants import Colors


class Obstacle:
    def __init__(self, x, y, speed):
        self.height = 10
        self.width = 20
        self.x = x
        self.y = y
        self.speed = speed

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(surface, Colors.WHITE.value, self.rect)

    def tick(self):
        self.x -= self.speed

    def can_be_remove(self):
        return self.x + self.width < 0
