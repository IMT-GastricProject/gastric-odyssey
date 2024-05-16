from flask import Blueprint, request, jsonify
from repositories.QuestionRepository import QuestionRepository

update_question = Blueprint('update_question', __name__)

@update_question.route('/questions/update/<question_id>', methods=['PUT'])
def updateUser(question_id):
  try:
    if request.method == 'PUT':
      question_input = request.get_json()
      question_repository = QuestionRepository()
      question = question_repository.updateQuestion(question_id, question_input)

      if question:
        result = { question_id: { "title": question['title'], "content": question['content']} }
        return jsonify({ "question": result }), 200
      else:
        return {
          'message': 'Question not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try PUT.'
      }, 404
  except Exception as e:
    return {
        'message': f'Unexpected error. {str(e)}'
      }
  finally:
    question_repository.closeConnection()

