import pygame
from settings import SCREEN_SIZE
import requests
from random import choice

class Question_Box:
    def __init__(self, screen, questions, level, type, user):
        pygame.font.init()
        
        self.image = pygame.image.load("assets/questions/question_box.png")
        self.img = pygame.transform.scale(self.image, (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.level = level
        self.box_width = (SCREEN_SIZE[0]//2) - self.width//2
        self.box_height = (SCREEN_SIZE[1]//2) - self.height//2
        self.type = type
        self.font = pygame.font.SysFont('Poppins', int(self.box_width//18))
        self.selected_answer_id = ''
        self.pop_image = screen.blit(self.img, (self.box_width, self.box_height))
        self.screen = screen
        self.req = list(questions)
        self.question = choice(self.req)
        self.user = user
        self.question_header = self.question['title']
        self.answers = self.question['answers']
        self.display_box = True
        
        self.correct_answer = self.question['correct_answer_id']
        self.selected_text_rect = None

        self.format_header()
        self.format_answers()

    def format_header(self):
        text = self.question_header
        text_parts = []
        text_pos = 0
        for i in range(0, len(text), 95):
            text_parts.append(text[i:i+95])
        for part in range(len(text_parts)):
            if text_parts[part][0] == ' ':
                text_parts[part] = text_parts[part][1:]
        for j in range(len(text_parts)):
           self.question_header = text_parts[j]
           self.text_surface = self.font.render(self.question_header, True, (255, 255, 255))
           self.screen.blit(self.text_surface, ((self.box_width * 2) - (self.text_surface.get_width())/2, (self.box_height + self.text_surface.get_height() * 2) + text_pos))
           text_pos += (self.text_surface.get_height() * 2)

    def format_answers(self):
        position = 0    

        alternatives_list = ['a)', 'b)', 'c)', 'd)']
        for i in range(len(alternatives_list)):
            self.alternatives = self.font.render(alternatives_list[i], True, (255, 255, 255))
            self.screen.blit(self.alternatives, ((self.box_width + self.box_width // 5) - (self.alternatives.get_width()) / 2,
                                                (self.box_height + self.alternatives.get_height() * 12) + position))

            answer_text = self.question['answers'][i]['content']
            text_parts = [answer_text[j:j + 80] for j in range(0, len(answer_text), 80)]

            for part in text_parts:
                self.answer_text = self.font.render(part, True, (255, 255, 255))
                self.screen.blit(self.answer_text, (self.box_width + self.box_width // 4,
                                                    (self.box_height + self.alternatives.get_height() * 12) + position))
                position += self.alternatives.get_height() * 2





    def display_selected_text(self, selected_key):
        selected_font = pygame.font.SysFont('Poppins', 30)
    
        if self.selected_answer_id == self.correct_answer:
            selected_text_surface = selected_font.render(f"Alternativa selecionada: {selected_key.upper()} - Correta, abrindo porta...", True, (0, 255, 0))
            self.user.addPoints(5)
        else:
            selected_text_surface = selected_font.render(f"Alternativa selecionada: {selected_key.upper()} - Incorreta", True, (255, 0, 0))
            if self.user.getPoints() > 0:
                self.user.removePoints(2)
            elif self.user.getPoints() == 1:
                self.user.removePoints(1)
            else:
                None

        selected_text_rect = selected_text_surface.get_rect()

        selected_text_rect.topleft = (self.box_width, self.box_height + self.img.get_height() + 10)

        padding_x = 5
        padding_y = 5
        selected_text_rect.inflate_ip(padding_x * 2, padding_y * 2)

        selected_text_surface_rect = selected_text_surface.get_rect(center=selected_text_rect.center)

        pygame.draw.rect(self.screen, (30, 30, 30), selected_text_rect)

        self.screen.blit(selected_text_surface, selected_text_surface_rect)

        self.selected_text_rect = selected_text_rect

    def display(self):
        while self.display_box:
            if self.selected_answer_id == self.correct_answer:
                self.level.open_door[f'{self.type}'] = True
                self.level.update_map() 
                self.display_box = False
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.selected_answer_id = self.question['answers'][0]['answer_id']
                        self.display_selected_text("a")
                    if event.key == pygame.K_b:
                        self.selected_answer_id = self.question['answers'][1]['answer_id']
                        self.display_selected_text("b")
                    if event.key == pygame.K_c:
                        self.selected_answer_id = self.question['answers'][2]['answer_id']
                        self.display_selected_text("c")
                    if event.key == pygame.K_d:
                        self.selected_answer_id = self.question['answers'][3]['answer_id']
                        self.display_selected_text("d")
            

            pygame.display.flip()

    

