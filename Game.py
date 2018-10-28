import pygame, sys

from Board import Board
from Player import Player


class Game(object):
    def __init__(self):
        self.tps_max = 100.0  # ,max tikow na sekunde
        self.tps_delta = 0.0
        self.resolution = (720, 480)

        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()

        self.board = Board()
        temp_event = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN:
                    temp_event = event

            self.tps_delta += self.clock.tick() / 1000  # zwraca czas miedzy klatkami
            while self.tps_delta > 1 / self.tps_max:
                self.tps_delta -= 1 / self.tps_max
                self.tick(temp_event)
                temp_event = None

            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def tick(self, event):
        self.board.tick(event)

    def draw(self):
        self.board.draw(self.screen)


if __name__ == "__main__":  # czy prgrma zostal uruchomiony bezposrednio a nie zaimportowany
    Game()
