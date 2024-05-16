from flask import Blueprint, request
from repositories.UserRepository import UserRepository

remove_points_from_user = Blueprint('remove_points_from_user', __name__)

@remove_points_from_user.route('/points/remove/<user_id>/<points>', methods=['PATCH'])
def addPointsToUser(user_id, points):
  try:
    if request.method == 'PATCH':
      user_repository = UserRepository()
      user_repository.removePointsFromUser(user_id, points)

      return {
        'message': 'Points removed successfully.'
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