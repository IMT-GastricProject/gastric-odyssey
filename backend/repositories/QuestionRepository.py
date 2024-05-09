from utils.dbConnection import db_connection
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
    query = """SELECT id, title, content FROM questions WHERE id = %s"""
    query2 = """SELECT content FROM answers WHERE question_id = %s"""
    self.cursor.execute(query, (id,))

    question = self.cursor.fetchone()

    self.cursor.execute(query2, (id,))

    answer = self.cursor.fetchmany()

    return question, answer
  
  def getAllQuestions(self):
    query = """SELECT id, title, content FROM questions"""
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

    query = query[:-2] + " WHERE id = %s"
    data['id'] = id

    self.cursor.execute(query, tuple(data.values()))
    self.db_con.commit()

    return self.cursor.fetchone()
  
  def closeConnection(self):
    self.cursor.close()
    self.db_con.close()

    return