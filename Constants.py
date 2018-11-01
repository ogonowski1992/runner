from enum import Enum


class MoveDirections(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Colors(Enum):
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)


class Sizes(Enum):
    SQUARE_SIZE = 30
    MAP_WIDTH_PIXELS = 720
    MAP_HEIGHT_PIXELS = 480
    MAP_WIDTH_SQUARE = int(MAP_WIDTH_PIXELS / SQUARE_SIZE)
    MAP_HEIGHT_SQUARE = int(MAP_HEIGHT_PIXELS / SQUARE_SIZE)


class Actors(Enum):
    EMPTY_SPACE = 0
    ROCK = 1
    INDESTRUCTIBLE_ROCK = 2
    PLAYER = 3

    @staticmethod
    def create(value):
        if value == 0:
            return Actors.EMPTY_SPACE
        elif value == 1:
            return Actors.ROCK


class GameStatus(Enum):
    END = 1
    IS_GOING = 2
    PAUSE = 3
    BEGIN = 4
