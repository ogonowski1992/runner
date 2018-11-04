import pygame, sys

from Board import Board
from Constants import GameStatus
from Player import Player


class Game(object):
    def __init__(self):
        self.tps_max = 100.0  # ,max tikow na sekunde
        self.tps_delta = 0.0
        self.resolution = (720, 480)
        self.game_status = GameStatus.BEGIN

        pygame.init()
        self.font = pygame.font.SysFont("monospace", 50)

        self.splash = pygame.image.load('assets\\background\\splash.png')
        self.end = pygame.image.load('assets\\background\\end.png')
        self.bg = pygame.image.load('assets\\background\\bg_480.png')
        self.bgX = 0
        self.bgX2 = 2640
        self.bgSpeed = 1

        self.screen = pygame.display.set_mode(self.resolution)
        self.clock = pygame.time.Clock()
        self.board = Board()
        self.player = Player()

        self.enter_effect = pygame.mixer.Sound('assets\\sound\\bait.wav')
        pygame.mixer.music.load('assets\\sound\\bg.mp3')
        pygame.mixer.music.play(-1)

        while True:
            if self.game_status == GameStatus.IS_GOING:
                self.game_mode()
            elif self.game_status == GameStatus.PAUSE:
                self.pause_mode()
            elif self.game_status == GameStatus.END:
                self.end_mode()
            elif self.game_status == GameStatus.BEGIN:
                self.begin_game_mode()

            pygame.display.flip()

    def reset(self):
        self.player.reset()
        self.board.reset()

    def game_mode(self):
        for event in pygame.event.get():
            self.check_if_exit_game(event)
            self.check_for_pause(event)

        self.tps_delta += self.clock.tick() / 1000  # zwraca czas miedzy klatkami
        while self.tps_delta > 1 / self.tps_max:
            self.tps_delta -= 1 / self.tps_max

            self.player.move_actions()
            self.board.tick()
            if self.player.check_collisions_with_obstacles(self.board):
                self.game_status = GameStatus.END

        self.bgX -= self.bgSpeed
        self.bgX2 -= self.bgSpeed

        if self.bgX2 < -2640:
            self.bgX2 = self.bgX + 2640

        if self.bgX < -2640:
            self.bgX = self.bgX2 + 2640

        self.screen.blit(self.bg, (self.bgX, 0))
        self.screen.blit(self.bg, (self.bgX2, 0))
        self.board.draw(self.screen)
        self.player.draw(self.screen)

    def pause_mode(self):
        for event in pygame.event.get():
            self.check_if_exit_game(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                self.game_status = GameStatus.IS_GOING
                self.clock = pygame.time.Clock()

    def end_mode(self):
        for event in pygame.event.get():
            self.check_if_exit_game(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.reset()
                self.game_status = GameStatus.IS_GOING

        self.screen.blit(self.end, (0, 0))

    def begin_game_mode(self):
        for event in pygame.event.get():
            self.check_if_exit_game(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.enter_effect.play()
                self.game_status = GameStatus.IS_GOING
                self.clock = pygame.time.Clock()
                return
        self.screen.blit(self.splash, (0, 0))

    def check_if_exit_game(self, event):
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit(0)

    def check_for_pause(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            self.game_status = GameStatus.PAUSE


if __name__ == "__main__":  # czy progrma zostal uruchomiony bezposrednio a nie zaimportowany
    Game()
