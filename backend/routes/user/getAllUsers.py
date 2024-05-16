from flask import Blueprint, request, jsonify
from repositories.UserRepository import UserRepository

get_all_users = Blueprint('get_all_users', __name__)

@get_all_users.route('/users', methods=['GET'])
def getAllUsers():
  try:
    if request.method == 'GET':
      user_repository = UserRepository()
      users = user_repository.getAllUsers()
      
      result = {}
      for user in users:
        user_id, username, email, password, type, verification_code, isVerified, points = user
        result[user_id] = { "username": username,"email": email, "password": password, "type": type, "verification_code": verification_code, "isVerified": isVerified, "points": points }

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
    user_repository.closeConnection()