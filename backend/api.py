from flask import Flask
from services.emailSender import mail

from routes.user.createUser import create_user
from routes.user.getAllUsers import get_all_users
from routes.user.getSpecificUser import get_specific_user
from routes.user.deleteUser import delete_user
from routes.user.updateUser import update_user
from routes.user.verifyUser import verify_user

from routes.questions.createQuestion import create_question
from routes.questions.deleteQuestion import delete_question
from routes.questions.getAllQuestions import get_all_questions
from routes.questions.getSpecificQuestion import get_specific_question
from routes.questions.updateQuestion import update_question

from routes.questions.answers.addQuestionAnswer import add_question_answer
from routes.questions.answers.deleteAnswer import delete_answer
from routes.questions.answers.getQuestionAnswers import get_question_answers
from routes.questions.answers.updateAnswer import update_answer


class DataService:
  def __init__(self):
    self.app = Flask(__name__)

    self.app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    self.app.config['MAIL_PORT'] = 465
    self.app.config['MAIL_USERNAME'] = 'gastricodyssey@gmail.com'
    self.app.config['MAIL_PASSWORD'] = 'oawf mfec xuxg enms'
    self.app.config['MAIL_USE_SSL'] = True
    self.app.config['MAIL_USE_TSL'] = False

    mail.init_app(self.app)

    #rotas de usuários
    self.app.register_blueprint(create_user)
    self.app.register_blueprint(get_all_users)
    self.app.register_blueprint(get_specific_user)
    self.app.register_blueprint(delete_user)
    self.app.register_blueprint(update_user)
    self.app.register_blueprint(verify_user)

    # questions routes
    self.app.register_blueprint(create_question)
    self.app.register_blueprint(delete_question)
    self.app.register_blueprint(get_all_questions)
    self.app.register_blueprint(get_specific_question)
    self.app.register_blueprint(update_question)

    # answers routes
    self.app.register_blueprint(add_question_answer)
    self.app.register_blueprint(delete_answer)
    self.app.register_blueprint(get_question_answers)
    self.app.register_blueprint(update_answer)


  def run(self):
    self.app.run(debug=True)