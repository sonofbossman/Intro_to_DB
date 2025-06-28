import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()
import os

try:
  mydb = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD')
  )

  if mydb.is_connected():
    print("MySQL connection is successful.")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except Exception as e:
  print(e)
finally:
  if 'mydb' in locals() and mydb.is_connected():
    mycursor.close()
    mydb.close()
    print("MySQL connection is closed.")