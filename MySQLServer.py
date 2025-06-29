import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
import os

try:
  connection = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD')
  )

  if connection.is_connected():
    print("MySQL connection is successful.")
    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
  print(e)
finally:
  if connection.is_connected() and 'connection' in locals():
    mycursor.close()
    connection.close()
    print("MySQL connection is closed.")