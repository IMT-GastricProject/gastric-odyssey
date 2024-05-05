from flask import Flask, request, jsonify
from routes.user.createUser import create_user
from routes.user.getAllUsers import get_all_users
from routes.user.getSpecificUser import get_specific_user
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#rotas de usuários
app.register_blueprint(create_user)
app.register_blueprint(get_all_users)
app.register_blueprint(get_specific_user)

if __name__ == '__main__':
  app.run(debug=True)