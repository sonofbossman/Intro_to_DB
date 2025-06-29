import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
import os

try:
  connection = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('DB_PASSWORD')
  )

  if connection.is_connected():
    print("MySQL connection is successful.")
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
  print('Error connecting to database', e)
finally:
  if 'connection' in locals() and connection.is_connected():
    cursor.close()
    connection.close()
    print("MySQL connection is closed.")