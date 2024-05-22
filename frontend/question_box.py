import pygame
from settings import SCREEN_SIZE

class Question_Box:
    def __init__(self, screen):
      pygame.font.init()
      
      self.image = pygame.image.load("assets/questions/question_box.png")
      self.img = pygame.transform.scale(self.image, (SCREEN_SIZE[0]/3, SCREEN_SIZE[1]/3))
      self.width = self.img.get_width()
      self.height = self.img.get_height()

      self.box_width = (SCREEN_SIZE[0]/2) - self.width/2
      self.box_height = (SCREEN_SIZE[1]/2)- self.height/2

      self.font = pygame.font.SysFont('Poppins', int(self.box_width//40))

      self.pop_image = screen.blit(self.img, (self.box_width, self.box_height))

      self.question_header = 'Um tipo de semente necessita de bastante água nos dois primeiros meses após o plantio. Um produtor pretende estabelecer o melhor momento para o plantio desse tipo de semente, nos meses de outubro a março. Após consultar a previsão do índice mensal de precipitação de chuva (ImPC) da região onde ocorrerá o plantio, para o período chuvoso de 2020-2021, ele obteve os seguintes dados: '
      
      def format_header(text):
            text_parts = []
            text_pos = 0
            for i in range(0, len(text), 95):
                text_parts.append(text[i:i+95])
            for part in range(len(text_parts)):
                if text_parts[part][0] == ' ':
                    text_parts[part] = text_parts[part][1:]
                print(text_parts[part])
            for j in range(len(text_parts)):
               self.question_header = text_parts[j]
               self.text_surface = self.font.render(self.question_header, True, (255, 255, 255))
               screen.blit(self.text_surface, ((self.box_width + self.box_width/2) - (self.text_surface.get_width())/2, (self.box_height + self.text_surface.get_height() * 2) + text_pos))
               text_pos += (self.text_surface.get_height() * 2)
               
      format_header(self.question_header)
      

      

      





            