from flask import Blueprint, request, jsonify
from repositories.QuestionRepository import QuestionRepository

get_specific_question = Blueprint('get_specific_question', __name__)

@get_specific_question.route('/questions/<question_id>', methods=['GET'])
def getSpecificQuestion(question_id):
  try:
    if request.method == 'GET':
      question_repository = QuestionRepository()
      question = question_repository.getSpecificQuestion(question_id)

      print(question)

      if question:
        title, content = question
        result = { question_id: { "title": title[1], "content": title[2], "answers": content[0] } }
        return jsonify({ "question": result }), 200
      else:
        return {
          'message': 'Question not found.'
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
    question_repository.closeConnection()