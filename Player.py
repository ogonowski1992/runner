import pygame
from pygame.rect import Rect

from Constants import Colors, Sizes


def load_image(name):
    image = pygame.image.load(name)
    return image


class Player:
    def __init__(self):
        self.x = 50
        self.y = 200

        self.width = 60
        self.height = 100

        self.speedX = 0
        self.speedY = 0

        self.jumping = True

        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.clock = pygame.time.Clock()
        self.run_images = []
        self.jump_images = []

        for i in range(9):
            picture = pygame.transform.scale(load_image('assets\\player\\_Jump (' + str(i + 1) + ').png'), (80, 105))
            #pygame.image.save(picture, 'assets\\player\\_Jump (' + str(i + 1) + ').png')
            self.jump_images.append(picture)
            picture = pygame.transform.scale(load_image('assets\\player\\_Walk (' + str(i + 1) + ').png'), (80, 105))
            self.run_images.append(picture)
        self.index = 0

        self.time_for_animation_frame = 60
        self.tps_delta = 0

    def draw(self, surface):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.jumping is True:
            surface.blit(self.jump_images[self.index], self.rect)
        else:
            surface.blit(self.run_images[self.index], self.rect)

        pygame.draw.rect(surface, Colors.GREEN.value, self.rect, 2)

    def move_actions(self):
        self.tps_delta += self.clock.tick()  # zwraca czas miedzy klatkami
        if self.tps_delta > self.time_for_animation_frame:
            self.tps_delta = 0
            self.index += 1
            if self.index >= len(self.run_images):
                self.index = 0

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_SPACE] and self.jumping is False:
            self.speedY = -8
            self.jumping = True

        if self.y > 300:
            self.jumping = False
            self.speedY = 0
            self.y = 295

        if self.jumping is True:
            self.speedY = self.speedY + 0.2

        if pressed[pygame.K_LEFT]:
            self.speedX = -5
        elif pressed[pygame.K_RIGHT]:
            self.speedX = 5

        self.move()
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
        self.jumping = True
