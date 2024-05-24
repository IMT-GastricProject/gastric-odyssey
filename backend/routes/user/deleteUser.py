from flask import Blueprint, request
from repositories.UserRepository import UserRepository

delete_user = Blueprint('delete_user', __name__)

@delete_user.route('/users/delete/<id>', methods=['DELETE'])
def deleteUser(id): 
  user_repository = UserRepository()
  try:
    if request.method == 'DELETE':
      rowcount = user_repository.deleteUser(id)
      
      if rowcount:
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
    user_repository.closeConnection()
