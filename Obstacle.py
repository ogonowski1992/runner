import random

import pygame
from pygame.rect import Rect

from Constants import Colors


def load_image(name):
    image = pygame.image.load(name)
    return image


class Obstacle:
    def __init__(self, x, y, speed):
        self.height = 100
        self.width = 60
        self.x = x
        self.y = y
        self.speed = speed

        self.rect = Rect(self.x, self.y, self.width, self.height)

        self.clock = pygame.time.Clock()
        self.images = []

        sex = 'female'
        if random.randrange(10) > 5:
            sex = 'male'
        for i in range(9):
            picture = pygame.transform.scale(load_image('assets\\enemy\\' + sex + '\\_Walk (' + str(i + 1) + ').png'),
                                             (80, 105))
            # pygame.transform.flip()
            self.images.append(picture)

            self.index = 0
            self.time_for_animation_frame = 60
            self.tps_delta = 0

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y

        surface.blit(self.images[self.index], self.rect)
        pygame.draw.rect(surface, Colors.WHITE.value, self.rect, 2)

    def tick(self):
        self.tps_delta += self.clock.tick()  # zwraca czas miedzy klatkami
        if self.tps_delta > self.time_for_animation_frame:
            self.tps_delta = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0

        self.x -= self.speed

    def can_be_remove(self):
        return self.x + self.width < 0
