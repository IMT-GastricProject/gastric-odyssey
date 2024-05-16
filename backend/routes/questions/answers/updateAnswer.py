from flask import Blueprint, request, jsonify
from repositories.AnswerRepository import AnswerRepository

update_answer = Blueprint('update_answer', __name__)

@update_answer.route('/answers/update/<answer_id>', methods=['PUT'])
def updateAnswer(answer_id):
  try:
    if request.method == 'PUT':
      answer_input = request.get_json()
      answer_repository = AnswerRepository()
      answer = answer_repository.updateAnswer(answer_id, answer_input)

      if answer:
        title, content = answer[1], answer[2], answer[3], answer[4]
        result = { answer_id: { "title": title, "content": content } }
        return jsonify({ "answer": result }), 200
      else:
        return {
          'message': 'Answer not found.'
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
    answer_repository.closeConnection()
