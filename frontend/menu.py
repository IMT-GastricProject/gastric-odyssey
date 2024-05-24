import pygame, sys
from menuScripts.button import Button
from main import Game
from settings import WIDTH, HEIGHT

pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")
Icon = pygame.image.load("assets/menu/Burger.png")
pygame.display.set_icon(Icon)

BG = pygame.transform.scale(pygame.image.load("assets/menu/MenuImage.png"), (WIDTH, HEIGHT))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/menu/font.ttf", size)

def play():
    game = Game()
    game.run()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(35).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(450, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(450, 460), 
                            text_input="BACK", font=get_font(55), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = image=pygame.transform.scale(pygame.image.load("assets/menu/Logo.png"), (WIDTH/1.2, HEIGHT/1.2))
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/3.375))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/menu/JogarSair Rect.png"), pos=(WIDTH/2, HEIGHT/2), 
                            text_input="Jogar", font=get_font(int(WIDTH/30)), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/menu/Opcoes Rect.png"), pos=(WIDTH/2, HEIGHT/1.5), 
                            text_input="Opções", font=get_font(int(WIDTH/30)), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/menu/JogarSair Rect.png"), pos=(WIDTH/2, HEIGHT/1.22), 
                            text_input="Sair", font=get_font(int(WIDTH/30)), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()