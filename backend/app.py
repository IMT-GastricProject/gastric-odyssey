from flask import Flask, request, jsonify
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
sysuser = os.getenv('SYSUSER')
password = os.getenv('PASSWORD')
db = os.getenv('DB')

app = Flask(__name__)

#criar uma conexão com o banco
def db_connection():
  cnx = mysql.connector.connect(
    user=f'{sysuser}', 
    password=f'{password}',
    host=f'{host}',
    port=f'{port}',
    database=f'{db}'
  )
  return cnx

@app.route('/')
def hello_world():
    return 'Hello, World!'

#rota pra uma tabela temporária chamada usuários, criei só pra teste
@app.route('/users/create', methods=['POST'])
def createUser():
  try:
    if request.method == 'POST':
      conn = db_connection()
      cursor = conn.cursor()
      user = request.get_json()
      query = """INSERT INTO users (username, password) VALUES (%s, %s)"""
      data = (user['username'], user['password'])
      cursor.execute(query,data)
      conn.commit()
      return {
        'message': 'User created successfully.',
        'user': user
      }, 201
    else:
      return {
        'message': 'Method not allowed, try POST.'
      }, 404
  except:
    return {
      'message': 'Unexpected error.'
    }, 500
  finally:
    #fecha o cursor e a conexão
    cursor.close()
    conn.close()

@app.route('/users/<int:id>', methods=['GET'])
def getSpecificUser(id):
  try:
    if request.method == 'GET':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)
      
      query = """SELECT id, username, password FROM users WHERE id = %s"""
      cursor.execute(query, (id,))
      
      user = cursor.fetchone()

      if user:
        user_id, username, password = user
        result = { user_id: { "username": username, "password": password } }
        return jsonify({ "user": result }), 200
      else:
        return {
          'message': 'User not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try GET.'
      }, 404
  except:
    return {
        'message': 'Unexpected error.'
      }
  finally:
    cursor.close()
    db_con.close()
  
@app.route('/users', methods=['GET'])
def getAllUsers():
  try:
    if request.method == 'GET':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)
      
      query = """SELECT id, username, password FROM users"""
      cursor.execute(query)

      users = cursor.fetchall()
      
      result = {}
      for user in users:
        user_id, username, password = user
        result[user_id] = { "username": username, "password": password }

      return jsonify({ "users": result }), 200
    else:
      return {
        'message': 'Method not allowed, try GET.'
      }, 404
  except Exception as e:
    return {
      'message': f'Unexpected error. {str(e)}'
    }
  finally:
    cursor.close()
    db_con.close()

if __name__ == '__main__':
  app.run(debug=True)