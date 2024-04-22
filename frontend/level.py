import pygame
from settings import WORLD_MAP, TILESIZE
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites])
                if col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

    def run(self):
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super.__init__()
        self.display_surface = pygame.display.get_surface()

        def custom_draw(self):
            for sprite in self.sprites():
                self.display_surface.blit(sprite.image,sprite.rect)