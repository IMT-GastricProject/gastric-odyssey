import pygame, sys
from settings import SCREEN_SIZE, FPS
from level import *
import settings

#exibir jogo (com base nas configurações)
class Game:
    def __init__(self, screen_manager, user):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption('Gastric Odyssey')
        self.screen_manager = screen_manager
        self.clock = pygame.time.Clock()
        self.user = user
        self.level = Level(self.screen, self.screen_manager, self.user)
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
