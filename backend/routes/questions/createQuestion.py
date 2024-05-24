from flask import Blueprint, request
from repositories.QuestionRepository import QuestionRepository

create_question = Blueprint('create_question', __name__)

@create_question.route('/questions/create', methods=['POST'])
def createQuestion():
  question_repository = QuestionRepository()
  try:
    if request.method == 'POST':
      question = request.get_json()
      
      question_repository.createQuestion(question["title"], question["content"])

      return {
        'message': 'Question created successfully.',
        'question': question
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
    question_repository.closeConnection()