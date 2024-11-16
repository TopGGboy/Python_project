# 游戏主入口
from source import run_, setup
import pygame


def main():
    game = run_.Game()
    game.run()


if __name__ == '__main__':
    main()
    pygame.display.quit()
