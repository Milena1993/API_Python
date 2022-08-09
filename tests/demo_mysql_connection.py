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

# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, userId INT, 
# name VARCHAR(255), email VARCHAR(255), gender VARCHAR(255), status VARCHAR(255))")

sql = "INSERT INTO users (userId, name, email, gender, status) VALUES (%s, %s, %s, %s, %s)"
val = ("1544", "John", "John@gmail.com", "male", "active")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# mycursor = mydb.cursor()

# sql = "DELETE FROM users WHERE gender ='male'"

# mycursor.execute(sql)

# mydb.commit()



