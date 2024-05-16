from services.dbConnection import db_connection
from uuid import uuid4
from utils.generateCode import generateCode

class UserRepository:
  def __init__(self):
    self.db_con = db_connection()
    self.cursor = self.db_con.cursor(buffered=True)

  def createUser(self, username, email, password):
    username_nospaces = str(username).lower().replace(" ", "")
      
    user_code = generateCode()

    if str(email).lower().split('@')[1] == 'jpiaget.pro.br':
      query = """INSERT INTO users (id, username, email, password, type, verification_code, isVerified ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
      data = (str(uuid4()), username_nospaces, email, password, 1, user_code, 0) # Type 0 é aluno, 1 é professor. isVerified 0 é False e 1 é True.
    else:
      query = """INSERT INTO users (id, username, email, password, type, verification_code, isVerified ) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
      data = (str(uuid4()), username_nospaces, email, password, 0, user_code, 0) # Type 0 é aluno, 1 é professor. isVerified 0 é False e 1 é True.
    
    self.cursor.execute(query,data)
    self.db_con.commit()

    return user_code
  
  def deleteUser(self, id):
    query = """DELETE FROM users WHERE id=%s"""
    self.cursor.execute(query, (str(id),))
    self.db_con.commit()

    return self.cursor.rowcount
  
  def getAllUsers(self):
    query = """SELECT * FROM users"""
    self.cursor.execute(query)

    return self.cursor.fetchall()

  def getSpecificUser(self, id):
    query = """SELECT * FROM users WHERE id = %s"""
    self.cursor.execute(query, (id,))

    return self.cursor.fetchone()
  
  def verifyUser(self, id):
    self.cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = self.cursor.fetchone()
    if user:
      query = """UPDATE users SET isVerified = %s WHERE id = %s AND isVerified != %s"""
      data = (1,id,1)
      self.cursor.execute(query, data)
      self.db_con.commit()
      return True
    else:
      return False
  
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

  def addPointsToUser(self, user_id, points):
    query = "UPDATE users SET points = points + %s WHERE id = %s"
    data = (points, user_id)
    self.cursor.execute(query, data)
    self.db_con.commit()

    return

  def removePointsFromUser(self, user_id, points):
    query = "UPDATE users SET points = points - %s WHERE id = %s"
    data = (points, user_id)
    self.cursor.execute(query, data)
    self.db_con.commit()

    return

  def closeConnection(self):
    self.cursor.close()
    self.db_con.close()

    return