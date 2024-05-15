import pygame
from settings import WORLD_MAP, TILESIZE
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = Camera()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

# gerar o mapa
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites])
                elif col == 'p':
                    self.player = Player((x, y), [self.visible_sprites], self.obstacles_sprites)

#movimentação do player
    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


#configurações da câmera
class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0]//2
        self.half_height = self.display_surface.get_size()[1]//2
        self.offset = pygame.math.Vector2(100,150)

        self.floor_surface = pygame.image.load('assets/map.png').convert()
        self.floor_rect = self.floor_surface.get_rect(topleft= (0,0))
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surface, floor_offset_pos)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)