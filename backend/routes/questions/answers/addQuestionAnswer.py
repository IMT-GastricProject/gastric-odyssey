from flask import Blueprint, request
from repositories.AnswerRepository import AnswerRepository

add_question_answer = Blueprint('add_question_answer', __name__)

@add_question_answer.route('/questions/<question_id>/answers/create', methods=['POST'])
def addQuestionAnswer(question_id):
  answer_repository = AnswerRepository()
  try:
    if request.method == 'POST':
      answer = request.get_json()
      
      answer_repository.addQuestionAnswer(question_id, answer["content"])

      return {
        'message': 'Answer created successfully.',
        'answer': answer
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
    answer_repository.closeConnection()