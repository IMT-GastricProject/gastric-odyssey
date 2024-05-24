from flask import Blueprint, request, jsonify
from repositories.QuestionRepository import QuestionRepository
from repositories.AnswerRepository import AnswerRepository
get_all_questions = Blueprint('get_all_questions', __name__)

@get_all_questions.route('/questions', methods=['GET'])
def getAllQuestions():
  question_repository = QuestionRepository()
  try:
    if request.method == 'GET':
      questions = question_repository.getAllQuestions()
      answers_repository = AnswerRepository()
      result = {}
      for question in questions:
        all_answers = []
        questionid, title,  correct_answer, content = question
        answers = answers_repository.getQuestionAnswers(questionid)
        for answer in answers:
          answer_id, idquestion_answer, contentanswer = answer
          all_answers.append({"answer_id":  answer_id, "content": contentanswer})
        result[questionid] = { "title": title, "content": content, "correct_answer_id": correct_answer, "answers": all_answers }

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