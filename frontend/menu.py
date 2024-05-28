import pygame, sys
from menu_scripts.button import Button
from game import Game
from leaderboard import leaderboard_call
from alunos import alunos_call
from settings import WIDTH, HEIGHT
from user import Professor
class Menu:
    def __init__(self, user):
        pygame.init()

        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Menu")
        self.Icon = pygame.image.load("assets/menu/Burger.png")
        pygame.display.set_icon(self.Icon)
        self.user = user
        self.BG = pygame.transform.scale(pygame.image.load("assets/menu/MenuImage.png"), (WIDTH, HEIGHT))

    def get_font(self, size):
        return pygame.font.Font("assets/menu/font.ttf", size)

    def play(self):
        self.game = Game()
        self.game.run()
            
    def leaderboard(self):
        self.leaderboard = leaderboard_call()

    def alunos(self):
        self.alunos = alunos_call()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = image=pygame.transform.scale(pygame.image.load("assets/menu/Logo.png"), (WIDTH/1.2, HEIGHT/1.2))
            MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/3.375))

            PLAY_BUTTON = Button(image=pygame.image.load("assets/menu/JogarSair Rect.png"), pos=(WIDTH/2, HEIGHT/2), 
                                text_input="Jogar", font=self.get_font(int(WIDTH/35)), base_color="#d7fcd4", hovering_color="White")
            LEADERBOARD_BUTTON = Button(image=pygame.image.load("assets/menu/Leaderboard Rect.png"), pos=(WIDTH/2, HEIGHT/1.5), 
                                text_input="Leaderboard", font=self.get_font(int(WIDTH/35)), base_color="#d7fcd4", hovering_color="White")
            if isinstance(self.user, Professor):
                ALUNOS_BUTTON = Button(image=pygame.image.load("assets/menu/Leaderboard Rect.png"), pos=(WIDTH/1.13, HEIGHT/1.1),
                                    text_input="Alunos", font=self.get_font(int(WIDTH/35)), base_color="#d7fcd4", hovering_color="White")
            
            QUIT_BUTTON = Button(image=pygame.image.load("assets/menu/JogarSair Rect.png"), pos=(WIDTH/2, HEIGHT/1.22), 
                                text_input="Sair", font=self.get_font(int(WIDTH/35)), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)
            

            if 'ALUNOS_BUTTON' in locals():
                for button in [PLAY_BUTTON, LEADERBOARD_BUTTON, ALUNOS_BUTTON, QUIT_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(self.SCREEN)
            else:
                for button in [PLAY_BUTTON, LEADERBOARD_BUTTON, QUIT_BUTTON]:
                    button.changeColor(MENU_MOUSE_POS)
                    button.update(self.SCREEN)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.play()
                    if LEADERBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.leaderboard()
                    if 'ALUNOS_BUTTON' in locals():
                        if ALUNOS_BUTTON.checkForInput(MENU_MOUSE_POS):
                            self.alunos()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def run(self):
        self.main_menu()