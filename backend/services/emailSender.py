from flask_mail import Mail, Message

mail = Mail()

def emailSender(user_email, user_code):  
    email_content = f'Bem-vindo ao Gastric Odyssey! Seu código de verificação é: {user_code}'
    msg = Message(email_content, sender="gastricodyssey@outlook.com", recipients=[f'{user_email}'])

    mail.send(msg)