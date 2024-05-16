import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
sysuser = os.getenv('SYSUSER')
password = os.getenv('PASSWORD')
db = os.getenv('DB')

#criar uma conexão com o banco
def db_connection():
  cnx = mysql.connector.connect(
    user=f'{sysuser}', 
    password=f'{password}',
    host=f'{host}',
    port=f'{port}',
    database=f'{db}'
  )
  return cnx