import pygame
import time
import random

from pygame.constants import KEYDOWN
from pygame.rect import Rect

from Constants import MoveDirections, Colors, Sizes
from Player import Player




def main():
    pygame.init()

    clock = pygame.time.Clock()

    #    logo = pygame.image.load("logo32x32.png")
    #   pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    board = Board()

    screen = pygame.display.set_mode((720, 480))
    running = True
    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == pygame.K_d:
                    board.player.move_player(MoveDirections.RIGHT)
                if event.key == pygame.K_w:
                    board.player.move_player(MoveDirections.UP)
                if event.key == pygame.K_s:
                    board.player.move_player(MoveDirections.DOWN)
                if event.key == pygame.K_a:
                    board.player.move_player(MoveDirections.LEFT)

        screen.fill(Colors.BLACK.value)
        board.draw(screen)
        pygame.display.update()


if __name__ == "__main__":
    main()
