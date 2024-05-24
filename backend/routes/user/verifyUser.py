from flask import Blueprint, request, jsonify
from repositories.UserRepository import UserRepository

verify_user = Blueprint('verify_user', __name__)

@verify_user.route('/users/verify/<code>/<id>', methods=['PATCH'])
def verifyUser(code, id):
  user_repository = UserRepository()
  try:
    if request.method == 'PATCH':
      user_select = user_repository.getSpecificUser(id)
      
      if user_select:
        user_id, username, email, password, type, verification_code, isVerified, points = user_select
        if int(code) == verification_code:
          user = user_repository.verifyUser(id)

          if isVerified == 1:
            return {
            'message': 'User already verified.'
          }, 400
          else:
            return {
              'message': 'User successfully verified.'
            }, 200
        else:
          return {
            'message': 'Invalid verification code.'
          }
      else:
        return {
          'message': 'User not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try PATCH.'
      }, 404
    
  except Exception as e:
    return {
        'message': f'Unexpected error. {str(e)}'
      }
  finally:
    user_repository.closeConnection()

