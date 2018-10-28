import time

import pygame
from pygame.rect import Rect

from Constants import MoveDirections, Colors, Sizes, Actors


class Player:
    def __init__(self, bord):
        self.x = 0
        self.y = 0
        self.lastTime = time.time() * 1000
        self.bord = bord

    def draw(self, surface):
        pygame.draw.rect(surface, Colors.GREEN.value,
                         Rect(self.x * Sizes.SQUARE_SIZE.value, self.y * Sizes.SQUARE_SIZE.value,
                              Sizes.SQUARE_SIZE.value,
                              Sizes.SQUARE_SIZE.value))

    def can_move_to(self, x, y):
        if x < 0 or y < 0 or x > Sizes.MAP_WIDTH_SQUARE.value or y > Sizes.MAP_HEIGHT_SQUARE.value:
            return False
        if self.bord.bord[x][y] == Actors.EMPTY_SPACE:
            return True
        return False

    def tick(self, event):
        if event is not None:
            if event.key == pygame.K_UP:
                if self.can_move_to(self.x, self.y - 1):
                    self.y -= 1
            elif event.key == pygame.K_DOWN:
                if self.can_move_to(self.x, self.y + 1):
                    self.y += 1
            elif event.key == pygame.K_LEFT:
                if self.can_move_to(self.x - 1, self.y):
                    self.x -= 1
            elif event.key == pygame.K_RIGHT:
                if self.can_move_to(self.x + 1, self.y):
                    self.x += 1
            elif event.key == pygame.K_SPACE:
                self.bord.put_bomb(self.x, self.y)
