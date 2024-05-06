from utils.dbConnection import db_connection
from uuid import uuid4

class UserRepository:
  def __init__(self):
    self.db_con = db_connection()
    self.cursor = self.db_con.cursor(buffered=True)

  def createUser(self, username, email, password):
    username_nospaces = str(username).lower().replace(" ", "")
      
    if str(email).lower().split('@')[1] == 'jpiaget.pro.br':
      query = """INSERT INTO users (id, username, email, password, type ) VALUES (%s, %s, %s, %s, %s)"""
      data = (str(uuid4()), username_nospaces, email, password, 1) # 0 é aluno, 1 é professor.
    else:
      query = """INSERT INTO users (id, username, email, password, type ) VALUES (%s, %s, %s, %s, %s)"""
      data = (str(uuid4()), username_nospaces, email, password, 0) # 0 é aluno, 1 é professor.
    
    self.cursor.execute(query,data)
    self.db_con.commit()

    return
  
  def deleteUser(self, id):
    query = """DELETE FROM users WHERE id=%s"""
    self.cursor.execute(query, (str(id),))
    self.db_con.commit()

    return self.cursor.rowcount
  
  def getAllUsers(self):
    query = """SELECT id, username, email, password, type FROM users"""
    self.cursor.execute(query)

    return self.cursor.fetchall()

  def getSpecificUser(self, id):
    query = """SELECT id, username, email, password, type FROM users WHERE id = %s"""
    self.cursor.execute(query, (id,))

    return self.cursor.fetchone()

  def updateUser(self, id, user_input):
    data = {}
    query = "UPDATE users SET "

    if 'username' in user_input:
      query += "username = %s, "
      username_nospaces = str(user_input['username']).lower().replace(" ", "")
      data['username'] = username_nospaces

    if 'email' in user_input:
      query += "email = %s, "
      data['email'] = user_input['email']

    if 'password' in user_input:
      query += "password = %s, "
      data['password'] = user_input['password']

    if 'type' in user_input:
      query += "type = %s, "
      data['type'] = user_input['type']
      
    query = query.rstrip(', ')
    query += " WHERE id = %s"
    data['id'] = id

    self.cursor.execute(query, tuple(data.values()))
    self.db_con.commit()

    self.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = self.cursor.fetchone()

    return user

  def closeConnection(self):
    self.cursor.close()
    self.db_con.close()

    return