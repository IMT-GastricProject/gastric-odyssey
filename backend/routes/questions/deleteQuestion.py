from flask import Blueprint, request
from repositories.QuestionRepository import QuestionRepository

delete_question = Blueprint('delete_question', __name__)

@delete_question.route('/question/delete/<question_id>', methods=['DELETE'])
def deleteQuestion(question_id): 
  try:
    if request.method == 'DELETE':
      question_repository = QuestionRepository()
      rowcount = question_repository.deleteQuestion(question_id)
      
      if rowcount:
        return {
          'message': 'Question successfully deleted'
        }, 200
      else:
        return {
          'message': 'Question not found.'
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
    question_repository.closeConnection()
