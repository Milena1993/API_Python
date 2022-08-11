import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin12345",
  database="gorestusers"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users (userId, name, email, gender, status) VALUES (%s, %s, %s, %s, %s)"
val = ("1544", "John", "John@gmail.com", "male", "active")
mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM users")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)



