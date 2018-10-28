import pygame
import random

from pygame.rect import Rect

from Bomb import Bomb
from Constants import Sizes, Colors, Actors
from Player import Player


class Board:
    def __init__(self):
        self.bord = [[self.generateMap(x, y) for x in range(Sizes.MAP_HEIGHT_SQUARE.value)] for y in
                     range(Sizes.MAP_WIDTH_SQUARE.value)]
        self.player = Player(self)
        self.bombs = []

    def generateMap(self, x, y):
        if x == 0 and y == 0:
            return Actors.EMPTY_SPACE
        elif x % 2 == 1 and y % 2 == 1:
            return Actors.INDESTRUCTIBLE_ROCK
        elif x < 3 and y < 3:
            return Actors.EMPTY_SPACE
        else:
            return Actors.create(random.randint(0, 1))

    def draw(self, surface):
        for row in range(Sizes.MAP_WIDTH_SQUARE.value):
            for element in range(Sizes.MAP_HEIGHT_SQUARE.value):
                if self.bord[row][element] == Actors.ROCK:
                    pygame.draw.rect(surface, Colors.RED.value,
                                     Rect(row * Sizes.SQUARE_SIZE.value, element * Sizes.SQUARE_SIZE.value,
                                          Sizes.SQUARE_SIZE.value,
                                          Sizes.SQUARE_SIZE.value))
                elif self.bord[row][element] == Actors.EMPTY_SPACE:
                    pygame.draw.rect(surface, Colors.BLACK.value,
                                     Rect(row * Sizes.SQUARE_SIZE.value, element * Sizes.SQUARE_SIZE.value,
                                          Sizes.SQUARE_SIZE.value,
                                          Sizes.SQUARE_SIZE.value))
                elif self.bord[row][element] == Actors.INDESTRUCTIBLE_ROCK:
                    pygame.draw.rect(surface, Colors.YELLOW.value,
                                     Rect(row * Sizes.SQUARE_SIZE.value, element * Sizes.SQUARE_SIZE.value,
                                          Sizes.SQUARE_SIZE.value,
                                          Sizes.SQUARE_SIZE.value))
        for b in self.bombs:
            b.draw(surface)
        self.player.draw(surface)

    def put_bomb(self, x, y):
        self.bombs.append(Bomb(self, x, y))

    def tick(self, event):
        self.player.tick(event)
