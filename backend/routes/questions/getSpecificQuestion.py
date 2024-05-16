from flask import Blueprint, request, jsonify
from repositories.QuestionRepository import QuestionRepository
from repositories.AnswerRepository import AnswerRepository
get_specific_question = Blueprint('get_specific_question', __name__)

@get_specific_question.route('/questions/<question_id>', methods=['GET'])
def getSpecificQuestion(question_id):
  try:
    if request.method == 'GET':
      question_repository = QuestionRepository()
      question = question_repository.getSpecificQuestion(question_id)
      answers_repository = AnswerRepository()
      print(question)

      if question:
        questionid, title, content, correct_answer = question
        answers = answers_repository.getQuestionAnswers(question_id)
        all_answers = []
        for answer in answers:
          answer_id, answerid, answer_content = answer
          all_answers.append({"answer_id": answer_id, "content":answer_content})

        result = { question_id: { "title": title, "content": content, "correct_answer_id": correct_answer, "answers": all_answers } }
        return result, 200
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