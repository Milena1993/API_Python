import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin12345",
  database="gorestusers"
)
# mycursor = mydb.cursor()
# # mycursor.execute("CREATE DATABASE gorestusers")
# mycursor.execute("SHOW DATABASES")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, userId INT, name VARCHAR(255), email VARCHAR(255), gender VARCHAR(255), status VARCHAR(255))")