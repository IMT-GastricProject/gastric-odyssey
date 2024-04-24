import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups, obstacle_sprites):
        super().__init__(groups)
        #define a imagem inicial do sprite do player, ela é modificada a cada mudança de direção, usando o método directionChange 
        self.directionChange('player_right')
        #rect é o retângulo que forma a imagem do sprite. É diferente da hitbox
        self.rect = self.image.get_rect(topleft = pos)
        #hitbox flúida para o personagem (leva em consideração a existência do rect)
        self.hitbox = self.rect.inflate(-26,-26)
        #define a direção como um vetor de duas dimensões (x,y)
        self.direction = pygame.math.Vector2()
        #define a velocidade da qual o sprite se movimenta, pois é multiplicado pelo valor do vetor direction
        self.speed = 5
        #define o obstacle_sprites que armazena os obstáculos que o player colide, que é passado como argumento de Player
        self.obstacle_sprites = obstacle_sprites

    #função para facilitar a mudança da imagem ao mudar a direção do sprite
    def directionChange(self, sprite_img):
        self.image = pygame.image.load(f'./assets/{sprite_img}.png').convert_alpha()

    def input(self):
        #detecta caso uma tecla seja pressionada
        keys = pygame.key.get_pressed()

        #armazena todas as teclas que podem ser utilizadas para realizar cada função do personagem.
        forward_keys = [pygame.K_w, pygame.K_UP]
        backward_keys = [pygame.K_s, pygame.K_DOWN]
        left_keys = [pygame.K_a, pygame.K_LEFT]
        right_keys = [pygame.K_d, pygame.K_RIGHT]

        if any(keys[key] for key in forward_keys):
            self.direction.y = -1
            self.directionChange('player_forward')
        elif any(keys[key] for key in backward_keys):
            self.direction.y = 1
            self.directionChange('player_backward')
        else:
            self.direction.y = 0

        if any(keys[key] for key in left_keys):
            self.direction.x = -1
            self.directionChange('player_left')
        elif any(keys[key] for key in right_keys):
            self.direction.x = 1
            self.directionChange('player_right')
        else:
            self.direction.x = 0
        
    def move(self, speed):
        #corrige o aumento de velocidade do personagem caso pressionado botões tanto do eixo x, quanto do eixo y
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    def update(self):
        self.input()
        self.move(self.speed)