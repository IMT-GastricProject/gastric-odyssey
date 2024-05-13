from flask import Flask
from utils.emailSender import mail

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

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'gastricodyssey@gmail.com'
app.config['MAIL_PASSWORD'] = 'oawf mfec xuxg enms'
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TSL'] = False


mail.init_app(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#rotas de usuários
app.register_blueprint(create_user)
app.register_blueprint(get_all_users)
app.register_blueprint(get_specific_user)
app.register_blueprint(delete_user)
app.register_blueprint(update_user)
app.register_blueprint(verify_user)

# questions routes
app.register_blueprint(create_question)
app.register_blueprint(delete_question)
app.register_blueprint(get_all_questions)
app.register_blueprint(get_specific_question)
app.register_blueprint(update_question)

# answers routes
app.register_blueprint(add_question_answer)
app.register_blueprint(delete_answer)
app.register_blueprint(get_question_answers)
app.register_blueprint(update_answer)

if __name__ == '__main__':
  app.run(debug=True)