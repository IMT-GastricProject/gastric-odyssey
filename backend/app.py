from flask import Flask, request
from supabase_package.client import supabase

app = Flask(__name__)

@app.route('/users/create', methods=['POST'])
def users():
  if request.method == 'POST':
    user_email = request.form.get('email')
    user_password = request.form.get('password')

    supabase.auth.sign_up(credentials={ 'email': user_email, 'password': user_password })

    return {
      'message': 'User created successfully.'
    }, 201
  else:
    return {
      'message': 'Method not allowed, try POST.'
    }, 404

if __name__ == '__main__':
  app.run(debug=True)