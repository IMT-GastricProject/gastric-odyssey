import requests
from settings import API_URL

class Usuario:
  def __init__(self):
    self.username = ''
    self.email = ''
    self.password = ''

class Aluno(Usuario):
  def __init__(self):
    self.points = 0

class Professor(Usuario):
  def deletarAluno(self,id):
    requests.delete(f'{API_URL}/users/delete/{id}')