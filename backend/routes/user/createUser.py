from flask import Blueprint, request, jsonify
from utils.dbConnection import db_connection
import uuid

create_user = Blueprint('create_user', __name__)

@create_user.route('/users/create', methods=['POST'])
def createUser():
  try:
    if request.method == 'POST':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)

      user = request.get_json()
      username_nospaces = str(user['username']).lower().replace(" ", "")
      
      if str(user['email']).lower().split('@')[1] == 'jpiaget.pro.br':
        query = """INSERT INTO users (id, username, email, password, type ) VALUES (%s, %s, %s, %s, %s)"""
        data = (str(uuid.uuid4()), username_nospaces, user['email'], user['password'], 1) # 0 é aluno, 1 é professor.
      else:
        query = """INSERT INTO users (id, username, email, password, type ) VALUES (%s, %s, %s, %s, %s)"""
        data = (str(uuid.uuid4()), username_nospaces, user['email'], user['password'], 0) # 0 é aluno, 1 é professor.

      cursor.execute(query,data)
      db_con.commit()

      return {
        'message': 'User created successfully.',
        'user': user
      }, 201
    else:
      return {
        'message': 'Method not allowed, try POST.'
      }, 404
  except Exception as e:
    return {
      'message': f'Unexpected error. {str(e)}'
    }, 500
  finally:
    #fecha o cursor e a conexão
    cursor.close()
    db_con.close()