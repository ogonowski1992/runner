import pygame
from pygame.rect import Rect

from Constants import Colors, Sizes


class Bomb(object):
    def __init__(self, board, x, y):
        self.y = y
        self.x = x
        self.board = board

    def draw(self, surface):
        pygame.draw.rect(surface, Colors.BLUE.value,
                         Rect(self.x * Sizes.SQUARE_SIZE.value, self.y * Sizes.SQUARE_SIZE.value,
                              Sizes.SQUARE_SIZE.value,
                              Sizes.SQUARE_SIZE.value))
