from flask import Blueprint, request
from repositories.UserRepository import UserRepository
from services.emailSender import emailSender

create_user = Blueprint('create_user', __name__)

@create_user.route('/users/create', methods=['POST'])
def createUser():
  user_repository = UserRepository()
  try:
    if request.method == 'POST':
      user = request.get_json()
      
      code = user_repository.createUser(user["username"], user["email"], user["password"])
      
      emailSender(user["email"], str(code))

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