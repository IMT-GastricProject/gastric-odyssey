import requests
from settings import API_URL

class Aluno():
  def __init__(self, user_data, user_id):
    self.user_data = user_data
    self.user_data['id'] = user_id
    self.points = 0
    
  def getUser(self):
    return self.user_data

  def addPoints(self, points):
    self.points += points

  def removePoints(self, points):
    if self.points > 0:
      self.points -= points

  def setPoints(self,points):
    self.points = points
  
  def getPoints(self):
    return self.points

class Professor(Aluno):
  def deletarAluno(self,id):
    requests.delete(f'{API_URL}/users/delete/{id}')