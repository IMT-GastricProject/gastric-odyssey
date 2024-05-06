from flask import Blueprint, request, jsonify
from utils.dbConnection import db_connection

update_user = Blueprint('update_user', __name__)

@update_user.route('/users/update/<id>', methods=['PUT'])
def updateUser(id):
  try:
    if request.method == 'PUT':
      db_con = db_connection()
      cursor = db_con.cursor(buffered=True)

      user_input = request.get_json()

      data = {}
      query = "UPDATE users SET "

      if 'username' in user_input:
        query += "username = %s, "
        data['username'] = user_input['username']

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

      cursor.execute(query, tuple(data.values()))
      db_con.commit()

      cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
      user = cursor.fetchone()

      if user:
        username, email, password, type = user[1], user[2], user[3], user[4]
        result = { id: { "username": username, "email": email, "password": password, "type": type } }
        return jsonify({ "user": result }), 200
      else:
        return {
          'message': 'User not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try PUT.'
      }, 404
  except Exception as e:
    return {
        'message': f'Unexpected error. {str(e)}'
      }
  finally:
    cursor.close()
    db_con.close()

