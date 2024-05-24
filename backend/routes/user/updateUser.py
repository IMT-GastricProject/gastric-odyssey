from flask import Blueprint, request, jsonify
from repositories.UserRepository import UserRepository

update_user = Blueprint('update_user', __name__)

@update_user.route('/users/update/<id>', methods=['PUT'])
def updateUser(id):
  user_repository = UserRepository()
  try:
    if request.method == 'PUT':
      user_input = request.get_json()
      user = user_repository.updateUser(id, user_input)

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
    user_repository.closeConnection()

