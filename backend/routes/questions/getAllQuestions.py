from flask import Blueprint, request, jsonify
from repositories.QuestionRepository import QuestionRepository

get_all_questions = Blueprint('get_all_questions', __name__)

@get_all_questions.route('/questions', methods=['GET'])
def getAllQuestions():
  try:
    if request.method == 'GET':
      question_repository = QuestionRepository()
      questions = question_repository.getAllQuestions()
      
      result = {}
      for question in questions:
        id, title, content = question
        result[id] = { "title": title, "content": content }

      return jsonify({ "questions": result }), 200
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