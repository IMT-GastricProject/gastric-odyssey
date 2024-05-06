from flask import Blueprint, request
from repositories.UserRepository import UserRepository

create_user = Blueprint('create_user', __name__)

@create_user.route('/users/create', methods=['POST'])
def createUser():
  try:
    if request.method == 'POST':
      user = request.get_json()
      
      user_repository = UserRepository()
      user_repository.createUser(user["username"], user["email"], user["password"])

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
    user_repository.closeConnection()