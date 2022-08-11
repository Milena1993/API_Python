from urllib import response
import requests
from config import API_TOKEN, BASE_URL
from assertpy.assertpy import assert_that
from uuid import uuid4
from json import dumps
import pytest
import mysql.connector
import json
import pymysql



def test_get_users():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin12345",
    database="gorestusers"
    )
    mycursor = mydb.cursor()

    get_response = requests.get(BASE_URL)
    response_text = get_response.json()
    print(response_text)
    print(len(response_text))
 
    for i in response_text:
        id_list = i['id']
        name_list= i['name']
        email_list =i['email']
        gender_option= i['gender']
        status_option=i['status']       
        mycursor.execute("INSERT INTO users (userId, name, email, gender, status) VALUES (%s, %s, %s, %s, %s)", (id_list, name_list, email_list, gender_option, status_option))
        mydb.commit()
    
    mycursor.execute("SELECT * FROM users WHERE userId=3904")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    



