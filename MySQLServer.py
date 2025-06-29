# import mysql.connector
# from mysql.connector import Error
# from dotenv import load_dotenv
# load_dotenv()
# import os

# try:
#   connection = mysql.connector.connect(
#     host=os.getenv('HOST'),
#     user=os.getenv('USER'),
#     password=os.getenv('DB_PASSWORD')
#   )

#   if connection.is_connected():
#     print("MySQL connection is successful.")
#     cursor = connection.cursor()
#     cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
#     print("Database 'alx_book_store' created successfully!")
# except Exception as e:
#   print('Error connecting to database', e)
# finally:
#   if 'connection' in locals() and connection.is_connected():
#     cursor.close()
#     connection.close()
#     print("MySQL connection is closed.")

import mysql.connector
from dotenv import load_dotenv
import os

try:
  # Load environment variables from .env file
  load_dotenv()
  db_password = os.getenv('DB_PASSWORD')

  connection = mysql.connector.connect(host='localhost', user='root', password=db_password)

  # check if there is connection
  if connection.is_connected():

    # create a cursor
    cursor = connection.cursor()

    # select the database
    cursor.execute('CREATE DATABASE IF NOT EXISTS alx_book_store;')

    print("Database 'alx_book_store' created successfully")
  
# catch errors
except mysql.connector.Error as e:
  print('Error connecting to database', e)

finally:
  if connection.is_connected():
    cursor.close()
    connection.close()
    print('Closed connection to database')