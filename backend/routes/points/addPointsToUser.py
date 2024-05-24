from flask import Blueprint, request
from repositories.UserRepository import UserRepository

add_points_to_user = Blueprint('add_points_to_user', __name__)

@add_points_to_user.route('/points/add/<user_id>/<points>', methods=['PATCH'])
def addPointsToUser(user_id, points):
  user_repository = UserRepository()
  try:
    if request.method == 'PATCH':
      user_repository.addPointsToUser(user_id, points)

      return {
        'message': 'Points added successfully.'
      }, 200
    else:
      return {
        'message': 'Method not allowed, try PATCH.'
      }, 404
  except Exception as e:
    return {
      'message': f'Unexpected error. {str(e)}'
    }, 500
  finally:
    user_repository.closeConnection()