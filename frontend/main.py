import pygame, sys
from settings import SCREEN_SIZE, FPS
from level import *
import settings

#exibir jogo (com base nas configurações)
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption('Gastric Odyssey')
        self.clock = pygame.time.Clock()
        self.level = Level(self.screen)
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
