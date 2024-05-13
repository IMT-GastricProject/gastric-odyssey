from flask import Blueprint, request, jsonify
from repositories.UserRepository import UserRepository

get_specific_user = Blueprint('get_specific_user', __name__)

@get_specific_user.route('/users/<id>', methods=['GET'])
def getSpecificUser(id):
  try:
    if request.method == 'GET':
      user_repository = UserRepository()
      user = user_repository.getSpecificUser(id)

      if user:
        user_id, username, email, password, type, verification_code, isVerified = user
        result = { user_id: { "username": username, "email": email,"password": password, "type": type, "verification_code": verification_code, "isVerified": isVerified} }
        return jsonify({ "user": result }), 200
      else:
        return {
          'message': 'User not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try GET.'
      }, 404
  except Exception as e:
    return {
        'message': f'Unexpected error. {str(e)}'
      }
  finally:
    user_repository.closeConnection()