import pygame, sys

from Board import Board
from Constants import GameStatus
from Player import Player


class Game(object):
    def __init__(self):
        self.tps_max = 100.0  # ,max tikow na sekunde
        self.tps_delta = 0.0
        self.resolution = (720, 480)

        self.game_status = GameStatus.IS_GOING
        self.after_pause = False

        pygame.init()
        myfont = pygame.font.SysFont("monospace", 50)

        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.player = Player()

        temp_event = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    if self.game_status == GameStatus.IS_GOING:
                        self.game_status = GameStatus.PAUSE
                    elif self.game_status == GameStatus.PAUSE:
                        self.game_status = GameStatus.IS_GOING
                        self.after_pause = True
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    if self.game_status == GameStatus.END:
                        self.game_status = GameStatus.IS_GOING
                        self.reset()
                elif event.type == pygame.KEYDOWN:
                    temp_event = event

            if self.game_status == GameStatus.IS_GOING:
                self.tps_delta += self.clock.tick() / 1000  # zwraca czas miedzy klatkami
                if self.after_pause:
                    self.tps_delta = 1 / self.tps_max
                    self.after_pause = False
                while self.tps_delta > 1 / self.tps_max:
                    self.tps_delta -= 1 / self.tps_max
                    self.tick(temp_event)
                    temp_event = None

                self.screen.fill((0, 0, 0))
                self.draw()
                pygame.display.flip()
            elif self.game_status == GameStatus.END:
                self.screen.fill((50, 50, 50))
                label = myfont.render("Game Over, points: " + str(self.board.points), 1, (100, 100, 100))
                self.screen.blit(label, (20, 200))
                pygame.display.flip()

    def tick(self, temp_event):
        self.player.move_actions(self.board, temp_event)
        if self.player.check_collisions_with_obstacles(self.board):
            self.game_status = GameStatus.END
        self.board.tick()

    def draw(self):
        self.board.draw(self.screen)
        self.player.draw(self.screen)

    def reset(self):
        self.player.reset()
        self.board.reset()


if __name__ == "__main__":  # czy progrma zostal uruchomiony bezposrednio a nie zaimportowany
    Game()
