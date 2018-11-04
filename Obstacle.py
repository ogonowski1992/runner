import random

import pygame
from pygame.rect import Rect

from Constants import Colors, Dimensions


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

        self.scream_effect = [pygame.mixer.Sound('assets\\sound\\scream_1.wav'),
                              pygame.mixer.Sound('assets\\sound\\scream_2.wav'),
                              pygame.mixer.Sound('assets\\sound\\scream_3.wav')]

        speed_up = random.randint(0, 10) > 6
        if speed_up:
            self.speed = self.speed * Dimensions.ZOMBI_BOOST_SPEED_MULTIPLIER
            self.scream_effect[random.randint(0, 2)].play()

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
