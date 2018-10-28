import pygame
from pygame.rect import Rect

from Constants import Colors


class Board:
    def __init__(self):
        self.rect = Rect(0, 400, 720, 80)

    def draw(self, surface):
        pygame.draw.rect(surface, Colors.RED.value, self.rect)
