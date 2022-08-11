from cgitb import reset
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

def test_get_all_data(): 
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + API_TOKEN
    }
    response = requests.get(BASE_URL, headers=headers).json()
    return response
   

def create_new_guser():
    unique_name = f'User{str(uuid4())}'
    payload = dumps({
        "name": unique_name, 
        "gender":"male", 
        "email": unique_name + '@gmail.com', 
        "status":"active"
    })
    # delete content-type , endpoint returns 422 error
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': "Bearer " + API_TOKEN
    }
    post_response = requests.post(url=BASE_URL, data=payload, headers=headers)
    post_response_text = post_response.json()
    print(post_response_text)
    assert_that(post_response_text['name']) == unique_name
    assert_that(post_response.status_code).is_equal_to(requests.codes.created)
    return unique_name

def test_get_added_user():
    added_person = create_new_guser()
    print(added_person)
    response = test_get_all_data()
    added_user = search_created_user(response, added_person)[0]
    print(added_user)
    print("kkkkkk")
    get_url = f'{BASE_URL}/{added_user["id"]}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + API_TOKEN
    }
    get_response = requests.get(get_url, headers = headers)
    assert_that(get_response.status_code).is_equal_to(requests.codes.ok)
    return added_user['id']


def test_created_user_can_be_deleted():
    person_id = test_get_added_user()
    print(person_id)
    print("SSSSS")
    # deleted_user_id = person_name['id']
    delete_url = f'{BASE_URL}/{person_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': "Bearer " + API_TOKEN
    }
    delete_response = requests.delete(delete_url, headers = headers)
    assert_that(delete_response.status_code).is_equal_to(requests.codes.no_content)


def search_created_user(response, name):
    return [person for person in response if person['name'] == name]