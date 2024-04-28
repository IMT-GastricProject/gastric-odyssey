from flask import Flask, request, jsonify
import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
user = os.getenv('USER')
password = os.getenv('PASSWORD')
db = os.getenv('DB')

app = Flask(__name__)

#criar uma conexão com o banco
def db_connection():
  cnx = mysql.connector.connect(
    user=f'{user}', 
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
      data = (user['name'], user['password'])
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
      }
  finally:
    #fecha o cursor e a conexão
    cursor.close()
    conn.close()

if __name__ == '__main__':
  app.run(debug=True)