import mysql.connector
from mysql.connector import Error

try:
  mydb = mysql.connector.connect(
    host="localhost",
    user="root1",
    password="Jehovahoverdo@2024"
  )

  if mydb.is_connected():
    print("MySQL connection is successful.")
    dbcursor = mydb.cursor()
    dbcursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
    print("Database 'alx_book_store' created successfully!")
except Error as e:
  print(e)
finally:
  if 'mydb' in locals() and mydb.is_connected():
    dbcursor.close()
    mydb.close()
    print("MySQL connection is closed.")