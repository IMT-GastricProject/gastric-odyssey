import pygame
import requests
from settings import API_URL, HEIGHT, TILESIZE, WIDTH
from tile import Tile
from player import Player
from utils.import_csv_layout import import_csv_layout
class Level:
    def __init__(self, screen, screen_manager, user):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = Camera()
        self.obstacles_sprites = pygame.sprite.Group()
        self.pressure_plates = pygame.sprite.Group()
        self.dont_touch = pygame.sprite.Group()
        self.tchau = pygame.sprite.Group()
        self.screen = screen
        self.user = user
        self.screen_manager = screen_manager
        self.player_pos = (900,900)
        self.finish_or_not = False
        self.user_points = list(requests.get(f'{API_URL}/users/{self.user.getUser()['id']}').json().values())[0][f'{self.user.getUser()['id']}']['points']
        #liberar portas
        self.open_door = {
            'laringe': False,
            'faringe': False,
            'intestino_delgado': False,
            'intestino_delgado_2': False,
            'intestino_grosso': False,
            'intestino_grosso2': False,
            'intestino_grosso3': False
        }

        self.create_map()

    def teleport_player(self):
        self.visible_sprites = Camera()
        self.obstacles_sprites = pygame.sprite.Group()
        self.pressure_plates = pygame.sprite.Group()
        self.dont_touch = pygame.sprite.Group()
        self.player_pos = (900,900)

        self.create_map()

    def finish(self):
        if self.finish_or_not == False:
            if self.user.getPoints() > self.user_points:
                if self.user_points >= 0:
                    requests.patch(f'{API_URL}/points/remove/{self.user.getUser()['id']}/{self.user_points}')
                else:
                    requests.patch(f'{API_URL}/points/add/{self.user.getUser()['id']}/{abs(self.user_points)}')
                requests.patch(f'{API_URL}/points/add/{self.user.getUser()['id']}/{self.user.getPoints()}')
                
            self.user.setPoints(0)
            self.screen_manager.menu()
            self.finish_or_not = True

# gerar o mapa
    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('assets/csv/map_blocos.csv'),
            'teeth': import_csv_layout('assets/csv/map_dentes.csv'),
            'laringe': import_csv_layout('assets/csv/map_doors_laringe.csv'),
            'faringe': import_csv_layout('assets/csv/map_doors_faringe.csv'),
            'intestino_delgado': import_csv_layout('assets/csv/map_doors_intestino_delgado.csv'),
            'intestino_delgado_2': import_csv_layout('assets/csv/map_doors_intestino_delgado_2.csv'),
            'intestino_grosso': import_csv_layout('assets/csv/map_doors_intestino_grosso.csv'),
            'intestino_grosso2': import_csv_layout('assets/csv/map_doors_intestino_grosso2.csv'),
            'intestino_grosso3': import_csv_layout('assets/csv/map_doors_intestino_grosso3.csv'),
            'tchau': import_csv_layout('assets/csv/map_tchau.csv'),
            'dont_touch': import_csv_layout('assets/csv/map_dont_touch.csv'),
        }

        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        
                        if style == 'boundary':
                            Tile((x,y), [self.visible_sprites,self.obstacles_sprites], 'boundary', pygame.image.load('assets/textures/skin.png'))

                        if style == 'teeth':
                            Tile((x,y), [self.obstacles_sprites], 'teeth', pygame.image.load('assets/textures/tooth.png'))

                        if style == 'laringe':
                                if self.open_door['laringe'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'laringe', pygame.image.load('assets/textures/door.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'laringe', pygame.image.load('assets/textures/door_opened.png'))

                        if style == 'faringe':
                                if self.open_door['faringe'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'faringe', pygame.image.load('assets/textures/door.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'faringe', pygame.image.load('assets/textures/door_opened.png'))

                        if style == 'intestino_delgado':
                                if self.open_door['intestino_delgado'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'intestino_delgado', pygame.image.load('assets/textures/door_rotated.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'intestino_delgado', pygame.image.load('assets/textures/door_opened_rotated.png'))

                        if style == 'intestino_delgado_2':
                                if self.open_door['intestino_delgado_2'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'intestino_delgado_2', pygame.image.load('assets/textures/door.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'intestino_delgado_2', pygame.image.load('assets/textures/door_opened.png'))

                        if style == 'intestino_grosso':
                                if self.open_door['intestino_grosso'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'intestino_grosso', pygame.image.load('assets/textures/door.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'intestino_grosso', pygame.image.load('assets/textures/door_opened.png'))

                        if style == 'intestino_grosso2':
                                if self.open_door['intestino_grosso2'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'intestino_grosso2', pygame.image.load('assets/textures/door.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'intestino_grosso2', pygame.image.load('assets/textures/door_opened.png'))

                        if style == 'intestino_grosso3':
                                if self.open_door['intestino_grosso3'] == False:
                                    Tile((x,y), [self.visible_sprites,self.obstacles_sprites, self.pressure_plates], 'intestino_grosso3', pygame.image.load('assets/textures/door.png'))
                                else:
                                    Tile((x,y), [self.visible_sprites], 'intestino_grosso3', pygame.image.load('assets/textures/door_opened.png'))
                                    
                        if style == 'dont_touch':
                            Tile((x,y), [self.obstacles_sprites, self.dont_touch], 'dont_touch', pygame.image.load('assets/textures/door.png'))

                        if style == 'tchau':
                            Tile((x,y), [self.obstacles_sprites, self.tchau], 'tchau', pygame.image.load('assets/textures/door.png'))


                            
        self.player = Player(self.player_pos, [self.visible_sprites], self.obstacles_sprites, self.pressure_plates, self.dont_touch, self.tchau, self.screen,self.user,self)
        
    def update_map(self):
        self.visible_sprites = Camera()
        self.obstacles_sprites = pygame.sprite.Group()
        self.pressure_plates = pygame.sprite.Group()
        self.dont_touch = pygame.sprite.Group()
    
        self.player_pos = self.player.rect.topleft

        self.create_map()
        
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