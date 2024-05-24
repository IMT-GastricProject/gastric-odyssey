from flask import Blueprint, request, jsonify
from repositories.AnswerRepository import AnswerRepository

get_question_answers = Blueprint('get_question_answers', __name__)

@get_question_answers.route('/questions/<question_id>/answers', methods=['GET'])
def getQuestionAnswer(question_id):
  answer_repository = AnswerRepository()
  try:
    if request.method == 'GET':
      answers = answer_repository.getQuestionAnswers(question_id)
      result ={}
      if answers:
        for answer in answers:
          answer_id, id, content = answer
          result[answers.index(answer) + 1] = { "answer_id":  answer_id, "content": content  }
        return result, 200
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