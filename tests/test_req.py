from cgitb import reset
from unicodedata import name
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

def authorization():
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': "Bearer " + API_TOKEN
    }
    return headers

def invalid_authorization():
    headers = {
        'Accept': 'application/json',
        'Authorization': "Bearer " + API_TOKEN
    }
    return headers

def get_all_data(): 
    response = requests.get(BASE_URL, headers=authorization()).json()
    return response
   
def get_user_info():
    name = get_random_name()
    payload = dumps({
        "name": name, 
        "gender":"male", 
        "email": name + '@gmail.com', 
        "status":"active"
    })
    return payload

def get_random_name():
    name = f'User{str(uuid4())}'
    return name


# 201 status code-user is created
def create_new_guser():
    unique_name = get_random_name()
    payload = dumps({
        "name": unique_name, 
        "gender":"male", 
        "email": unique_name + '@gmail.com', 
        "status":"active"
    })
    
    post_response = requests.post(url=BASE_URL, data=payload, headers=authorization())
    post_response_text = post_response.json()
    print(post_response_text)
    assert_that(post_response_text['name']) == unique_name
    assert_that(post_response.status_code).is_equal_to(requests.codes.created)
    return unique_name

#422 status code: Data validation failed
def test_create_new_guser_422():
    post_response = requests.post(url=BASE_URL, data=get_user_info(), headers=invalid_authorization())
    print("status code is" + " " + str(post_response.status_code))
    
#401 status code: Authentication failed.
def test_create_new_guser_401():
    post_response = requests.post(url=BASE_URL, data=get_user_info())
    print("status code is" + " " + str(post_response.status_code))

#405 status code:  Method not allowed
def test_create_new_guser_415():
    post_response = requests.unlink(url=BASE_URL, data=get_user_info())
    print("status code is" + " " + str(post_response.status_code))

# 200 status code-everything worked as expected
def test_get_added_user():
    added_person = create_new_guser()
    print(added_person)
    response = get_all_data()
    added_user = search_created_user(response, added_person)[0]
    print(added_user)
    print("kkkkkk")
    get_url = f'{BASE_URL}/{added_user["id"]}'
    get_response = requests.get(get_url, headers = authorization())
    assert_that(get_response.status_code).is_equal_to(requests.codes.ok)
    assert_that(get_response.json()['name']) == added_person
    return added_user['id']

# Put request-data successfully changed
def test_change_created_user():
    person_id = test_get_added_user()
    print(person_id)
    print("ggheddfS")
    
    updated_url = f'{BASE_URL}/{person_id}'
    unique_name = f'User{str(uuid4())}'
    payload = dumps({
        "name": unique_name, 
        "gender":"male", 
        "email": unique_name + '@gmail.com', 
        "status":"inactive"
    })
    put_response = requests.put(updated_url, data=payload, headers = authorization())
    print(put_response.status_code)
    assert_that(put_response.status_code).is_equal_to(requests.codes.ok)
    return person_id

# 204 status code_User is deleted
def test_delete_created_user():
    updated_person_id = test_change_created_user()
    print(updated_person_id)
    print("SSSSS")
    delete_url = f'{BASE_URL}/{updated_person_id}'
    delete_response = requests.delete(delete_url, headers = authorization())
    assert_that(delete_response.status_code).is_equal_to(requests.codes.no_content)


def search_created_user(response, name):
    return [person for person in response if person['name'] == name]