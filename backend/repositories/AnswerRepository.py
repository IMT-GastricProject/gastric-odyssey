from services.dbConnection import db_connection
from uuid import uuid4

class AnswerRepository:
  def __init__(self):
    self.db_con = db_connection()
    self.cursor = self.db_con.cursor(buffered=True)
  
  def addQuestionAnswer(self, question_id, content):
    query = """INSERT INTO answers (id, question_id, content) VALUES (%s, %s, %s)"""
    data = (str(uuid4()), str(question_id), content)
    
    self.cursor.execute(query,data)
    self.db_con.commit()

    return
  
  def deleteAnswer(self, id, question_id):
    query = """DELETE FROM answers WHERE id=%s and question_id=%s"""
    self.cursor.execute(query, (id, question_id))
    self.db_con.commit()

    return self.cursor.rowcount
  
  def updateAnswer(self, id, answer_input):
    data = {}
    query = "UPDATE answers SET "

    if 'content' in answer_input:
      query += "content = %s, "
      data['content'] = answer_input['content']

    query = query[:-2] + " WHERE id = %s"
    data['id'] = id

    self.cursor.execute(query, tuple(data.values()))
    self.db_con.commit()

    return self.cursor.rowcount

  def getQuestionAnswers(self, question_id):
    query = """SELECT id, content FROM answers WHERE question_id = %s"""
    self.cursor.execute(query, (question_id,))

    return self.cursor.fetchall()
  
  def closeConnection(self):
    self.cursor.close()
    self.db_con.close()

    return