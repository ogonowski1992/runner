import time

import pygame
from pygame.rect import Rect

from Constants import MoveDirections, Colors, Sizes, Actors


class Player:
    def __init__(self):
        self.x = 50
        self.y = 200

        self.speedX = 0
        self.speedY = 0

        self.rect = Rect(self.x, self.y, 50, 100)

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(surface, Colors.GREEN.value, self.rect)

    def tick(self, board, event):
        if self.rect.colliderect(board.rect):
            self.speedY = 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            self.speedX = -5
        elif pressed[pygame.K_RIGHT]:
            self.speedX = 5

        if event is not None:
            if event.key == pygame.K_SPACE:
                self.speedY = -10

        self.move()

        self.speedY = self.speedY + 0.2
        self.speedX = self.speedX * 0.8

    def move(self):
        self.x += self.speedX
        self.y += self.speedY
