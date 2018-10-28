import time

import pygame
from pygame.rect import Rect

from Constants import MoveDirections, Colors, Sizes, Actors


class Player:
    def __init__(self):
        self.x = 50
        self.y = 200

        self.width = 50
        self.height = 100

        self.speedX = 0
        self.speedY = 0

        self.rect = Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(surface, Colors.GREEN.value, self.rect)

    def move_actions(self, board, event):
        if self.rect.colliderect(board.rect):
            self.speedY = 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.speedX = -5
        elif pressed[pygame.K_RIGHT]:
            self.speedX = 5

        if event is not None:
            if event.key == pygame.K_SPACE:
                self.speedY = -6

        self.move()

        self.speedY = self.speedY + 0.2
        self.speedX = self.speedX * 0.8

    def move(self):
        if self.x + self.speedX >= 0 and self.x + self.speedX + self.width <= Sizes.MAP_WIDTH_PIXELS.value:
            self.x += self.speedX
        self.y += self.speedY

    def check_collisions_with_obstacles(self, board):
        for o in board.obstacles:
            if self.rect.colliderect(o.rect):
                return True
        return False

    def reset(self):
        self.x = 50
        self.y = 200
        self.speedX = 0
        self.speedY = 0
