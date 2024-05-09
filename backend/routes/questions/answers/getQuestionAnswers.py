from flask import Blueprint, request, jsonify
from repositories.AnswerRepository import AnswerRepository

get_question_answers = Blueprint('get_question_answers', __name__)

@get_question_answers.route('/questions/<question_id>/answers', methods=['GET'])
def getQuestionAnswer(question_id):
  try:
    if request.method == 'GET':
      answer_repository = AnswerRepository()
      answers = answer_repository.getQuestionAnswers(question_id)

      if answers:
        answer_id, title, content = answers
        result = { answer_id: { "title": title, "content": content } }
        return jsonify({ "answer": result }), 200
      else:
        return {
          'message': 'Answer not found.'
        }, 404
    else:
      return {
        'message': 'Method not allowed, try GET.'
      }, 404
  except Exception as e:
    return {
        'message': f'Unexpected error. {str(e)}'
      }
  finally:
    answer_repository.closeConnection()