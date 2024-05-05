from flask import Blueprint, request, jsonify
from utils.dbConnection import db_connection

get_specific_user = Blueprint('get_specific_user', __name__)

@get_specific_user.route('/users/<id>', methods=['GET'])
def getSpecificUser(id):
  try:
    if request.method == 'GET':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)
      
      query = """SELECT id, username, password, type FROM users WHERE id = %s"""
      cursor.execute(query, (id,))
      
      user = cursor.fetchone()

      if user:
        user_id, username, password, type = user
        result = { user_id: { "username": username, "password": password, "type": type } }
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