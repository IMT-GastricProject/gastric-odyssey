from services.dbConnection import db_connection
from uuid import uuid4

class QuestionRepository:
  def __init__(self):
    self.db_con = db_connection()
    self.cursor = self.db_con.cursor(buffered=True)
  
  def createQuestion(self, title, content):
    query = """INSERT INTO questions (id, title, content) VALUES (%s, %s, %s)"""
    data = (str(uuid4()), title, content)
    
    self.cursor.execute(query,data)
    self.db_con.commit()

    return
  
  def getSpecificQuestion(self, id):
    query = """SELECT * FROM questions WHERE id = %s"""
    self.cursor.execute(query, (id,))

    question = self.cursor.fetchone()

    return question
  
  def getAllQuestions(self):
    query = """SELECT id, title, correct_answer, content FROM questions"""
    self.cursor.execute(query)

    return self.cursor.fetchall()
  
  def deleteQuestion(self, id):
    query = """DELETE FROM questions WHERE id=%s"""
    self.cursor.execute(query, (id,))
    self.db_con.commit()

    return self.cursor.rowcount
  
  def updateQuestion(self, id, question_input):
    data = {}
    query = "UPDATE questions SET "

    if 'title' in question_input:
      query += "title = %s, "
      data['title'] = question_input['title']

    if 'content' in question_input:
      query += "content = %s, "
      data['content'] = question_input['content']

    if 'correct_answer' in question_input:
      query += "correct_answer = %s, "
      data['correct_answer'] = question_input['correct_answer']

    query = query.rstrip(', ')

    query += " WHERE id = %s"
    data['id'] = id

    self.cursor.execute(query, tuple(data.values()))
    self.db_con.commit()

    return data
  
  def closeConnection(self):
    self.cursor.close()
    self.db_con.close()

    return