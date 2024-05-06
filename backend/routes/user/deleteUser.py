from flask import Blueprint, request, jsonify
from utils.dbConnection import db_connection

delete_user = Blueprint('delete_user', __name__)

@delete_user.route('/users/delete/<id>', methods=['DELETE'])
def deleteUser(id): 
  try:
    if request.method == 'DELETE':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)
      
      query = """DELETE FROM users WHERE id=%s"""
      cursor.execute(query, (str(id),))
      
      db_con.commit()
      
      if cursor.rowcount:
        return {
          'message': 'User successfully deleted'
        }, 200
      else:
        return {
          'message': 'User not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try DELETE.'
      }, 404
  except Exception as e:
    return {
        'message': f'Unexpected error. {str(e)}'
      }
  finally:
    cursor.close()
    db_con.close()
