import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('./assets/wall.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        #hitbox flúida para o bloco da classe em questão (leva em consideração a existência do rect)
        self.hitbox = self.rect.inflate(-10,-10)