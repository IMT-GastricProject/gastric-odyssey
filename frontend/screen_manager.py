from alunos import Alunos
from leaderboard import Leaderboard
from menu import Menu


class ScreenManager():
  def __init__(self,user):
    self.user = user
    self.current_screen = None
  def menu(self):
    self.current_screen = Menu(self.user,self)
    self.current_screen.run()
  def leaderboard(self):
    self.current_screen = Leaderboard(self)

  def alunos(self):
    self.current_screen = Alunos(self)