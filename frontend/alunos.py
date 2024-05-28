import pygame, sys
from menu_scripts.button import Button
from settings import WIDTH, HEIGHT

def alunos_call():
    pygame.init()

    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Alunos")
    Icon = pygame.image.load("assets/menu/Burger.png")
    pygame.display.set_icon(Icon)

    BG = pygame.transform.scale(pygame.image.load("assets/menu/MenuImage.png"), (WIDTH, HEIGHT))

    def get_font(size):
        return pygame.font.Font("assets/menu/font.ttf", size)

    def resize_image(image, width, height):
        return pygame.transform.scale(image, (width, height))

    def create_blurred_rect(width, height):
        rect_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        rect_surface.set_alpha(128)
        rect_surface.fill((0, 0, 0, 128))
        
        for _ in range(10):
            rect_surface = pygame.transform.smoothscale(rect_surface, (width // 2, height // 2))
            rect_surface = pygame.transform.smoothscale(rect_surface, (width, height))
        
        return rect_surface

    def back():
        while True:
            BACK_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("black")

            BACK_TEXT = get_font(35).render("This is the MENU screen.", True, "White")
            BACK_RECT = BACK_TEXT.get_rect(center=(450, 260))
            SCREEN.blit(BACK_TEXT, BACK_RECT)

            BACK_BACK = Button(image=None, pos=(450, 460), 
                                text_input="BACK", font=get_font(55), base_color="White", hovering_color="Green")

            BACK_BACK.changeColor(BACK_MOUSE_POS)
            BACK_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BACK.checkForInput(BACK_MOUSE_POS):
                        main_menu()

            pygame.display.update()

    def main_menu():
        scroll_offset = 0
        scroll_speed = 20
        is_scrolling = False
        scroll_bar_rect = pygame.Rect(0, 0, 20, 100)

        while True:
            SCREEN.blit(BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = pygame.transform.scale(pygame.image.load("assets/menu/Alunos.png"), (WIDTH/1.5, HEIGHT/1.5))
            MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH/2, HEIGHT/5))

            BACK_BUTTON = Button(image=pygame.image.load("assets/menu/Voltar Rect.png"), pos=(WIDTH/2, HEIGHT/1.2), 
                                text_input="Voltar", font=get_font(int(WIDTH/40)), base_color="#d7fcd4", hovering_color="White")

            SCREEN.blit(MENU_TEXT, MENU_RECT)

            blurred_rect = create_blurred_rect(int(SCREEN.get_width() * 0.817), int(SCREEN.get_height() * 0.5))
            rect_pos = blurred_rect.get_rect(center=(SCREEN.get_width() // 2, SCREEN.get_height() // 2))
            SCREEN.blit(blurred_rect, rect_pos)

            content_height = blurred_rect.get_height() * 2
            content_surface = pygame.Surface((blurred_rect.get_width(), content_height), pygame.SRCALPHA)
            content_surface.fill((255, 255, 255, 0)) 
            
            for i in range(20):
                text = get_font(20).render(f"Item {i+1}", True, (0, 0, 0))
                content_surface.blit(text, (20, i * 40 + 10))

            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                scroll_offset = min(scroll_offset + scroll_speed, content_height - blurred_rect.get_height())
            if keys[pygame.K_UP]:
                scroll_offset = max(scroll_offset - scroll_speed, 0)

            if is_scrolling:
                mouse_y = pygame.mouse.get_pos()[1]
                new_scroll_offset = int((mouse_y - rect_pos.top) / blurred_rect.get_height() * content_height)
                scroll_offset = max(0, min(new_scroll_offset, content_height - blurred_rect.get_height()))

            mask = pygame.Surface((blurred_rect.get_width(), blurred_rect.get_height()), pygame.SRCALPHA)
            mask.blit(content_surface, (0, -scroll_offset))
            SCREEN.blit(mask, rect_pos.topleft)

            scroll_bar_height = blurred_rect.get_height() * (blurred_rect.get_height() / content_height)
            scroll_bar_rect.height = scroll_bar_height
            scroll_bar_rect.top = rect_pos.top + (scroll_offset / content_height) * blurred_rect.get_height()
            scroll_bar_rect.right = rect_pos.right

            pygame.draw.rect(SCREEN, (200, 200, 200), scroll_bar_rect)

            BACK_BUTTON.changeColor(MENU_MOUSE_POS)
            BACK_BUTTON.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        back()
                    if scroll_bar_rect.collidepoint(event.pos):
                        is_scrolling = True
                if event.type == pygame.MOUSEBUTTONUP:
                    is_scrolling = False
                if event.type == pygame.MOUSEWHEEL:
                    scroll_offset = max(0, min(scroll_offset - event.y * scroll_speed, content_height - blurred_rect.get_height()))

            pygame.display.update()

    main_menu()