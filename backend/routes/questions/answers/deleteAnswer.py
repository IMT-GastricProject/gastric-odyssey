from flask import Blueprint, request
from repositories.AnswerRepository import AnswerRepository

delete_answer = Blueprint('delete_answer', __name__)

@delete_answer.route('/questions/<question_id>/answers/delete/<answer_id>', methods=['DELETE'])
def addQuestionAnswer(question_id, answer_id):
  try:
    if request.method == 'DELETE':      
      answer_repository = AnswerRepository()
      answer_repository.deleteAnswer(answer_id, question_id)

      return {
        'message': f'Answer from question {question_id} deleted successfully.'
      }, 201
    else:
      return {
        'message': 'Method not allowed, try DELETE.'
      }, 404
  except Exception as e:
    return {
      'message': f'Unexpected error. {str(e)}'
    }, 500
  finally:
    answer_repository.closeConnection()