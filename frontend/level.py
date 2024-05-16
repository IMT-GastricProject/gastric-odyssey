import pygame
from settings import TILESIZE
from tile import Tile
from player import Player
from utils.import_csv_layout import import_csv_layout
class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = Camera()
        self.obstacles_sprites = pygame.sprite.Group()

        self.create_map()

# gerar o mapa
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('assets/csv/map_blocos.csv'),
            'teeth': import_csv_layout('assets/csv/map_dentes.csv')
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.visible_sprites,self.obstacles_sprites], 'visible', pygame.image.load('assets/textures/skin.png'))
                        if style == 'teeth':
                            Tile((x,y), [self.obstacles_sprites], 'invisible', pygame.image.load('assets/textures/tooth.pngp))

        self.player = Player((900,900), [self.visible_sprites], self.obstacles_sprites)

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

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)