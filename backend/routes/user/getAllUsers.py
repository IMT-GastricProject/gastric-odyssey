from flask import Blueprint, request, jsonify
from utils.dbConnection import db_connection

get_all_users = Blueprint('get_all_users', __name__)

@get_all_users.route('/users', methods=['GET'])
def getAllUsers():
  try:
    if request.method == 'GET':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)
      
      query = """SELECT id, username, email, password, type FROM users"""
      cursor.execute(query)

      users = cursor.fetchall()
      
      result = {}
      for user in users:
        user_id, username, email, password, type = user
        result[user_id] = { "username": username,"email": email, "password": password, "type": type }

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