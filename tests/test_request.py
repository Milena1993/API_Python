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




# GET METHOD
# def test_get_all_data():
#     all_users=[]
#     r=requests.get(f'https://gorest.co.in/public/v1/users')
#     for i in range(1,(r.json()["meta"]["pagination"]["pages"])+1):
#         temp=requests.get(f'https://gorest.co.in/public/v1/users?page={i}')
#         temp=temp.json()
#         for j in temp["data"]:
#             all_users.append(dict(id=j["id"],name=j["name"],email=j["email"],gender=j["gender"],status=j["status"]))
#     print(all_users)

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
    with open('users.json', 'w') as json_file:
        json.dump(response_text, json_file)
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

    



# #POST METHOD

# def test_create_user():
#     # all_users = test_get_all_data()
#     unique_name = f'User{str(uuid4())}'
#     payload = dumps(
#         {"name": unique_name, 
#         "gender":"male", 
#         "email": unique_name + '@gmail.com', 
#         "status":"active"}
#     )
#     headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json',
#         'Authorization': "Bearer " + API_TOKEN
#     }
#     post_response = requests.post(url=BASE_URL, data=payload, headers=headers)
#     post_response_text = post_response.json()
#     print(post_response_text)
#     print("MMMM")
#     assert_that(post_response.status_code).is_equal_to(201)
#     print("SSSS")
#     names = [person for person in all_users if person['name'] == unique_name]
#     assert_that(names).contains(unique_name)
#     return unique_name
    


    
# # def test_user_is_added():
# #     unique_name = test_create_user()
# #     all_users = test_get_all_data()
# #     assert_that(all_users).contains(unique_name)
#     # print(len(all_users))
#     # print([person for person in all_users if person['name'] == unique_name])
#     # is_new_user_created = search_created_user(all_users, unique_name)
#     # assert_that(is_new_user_created).is_not_empty()
    
   

# # # DELETE METHOD
# # # def test_delete_user():
# # #     unique_name = test_create_user() 
# # #     all_users = requests.get(BASE_URL).json()
# # #     new_created_user = search_created_user(all_users,unique_name)[0]
# # #     person_to_be_deleted = new_created_user['id']
# # #     delete_url = f'{BASE_URL}/{person_to_be_deleted}'
# # #     response =requests.delete(delete_url)
# # #     assert_that(response.status_code).is_equal_to(204)

# # def search_created_user(all_users, name):
# #     return [person for person in all_users if person['name'] == name]