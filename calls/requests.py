from uuid import uuid4
from calls.data import Testdata
from config import API_TOKEN, BASE_URL
from assertpy.assertpy import assert_that
from json import dumps
import requests
import pytest
import json


class APIRequests(Testdata):
    
    def __init__(self):
        super().__init__()
        self.base_url = BASE_URL
        self.header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + API_TOKEN
    }   
        self.invalidheaders = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + API_TOKEN
        }

        self.name = self.unique_name
        self.payload = dumps({
            "name": self.name, 
            "gender": self.gender,
            "email": self.name + '@gmail.com', 
            "status":self.status
        })
        self.updated_payload = dumps({
            "name": self.name, 
            "gender": self.gender,
            "email": self.name + '@gmail.com', 
            "status":self.diff_status
        })
        
    def get_all_data(self): 
        self.get_all_users = requests.get(self.base_url, headers = self.header)
        return self.get_all_users


    def create_new_guser(self):
        self.post_response = requests.post(self.base_url, data = self.payload, headers = self.header)
        self.post_response_text = self.post_response.json()
        self.unique_name = self.post_response_text['name']
        return self.unique_name , self.post_response.status_code
   
       
    def create_new_guser_with_invalid_data(self):
        self.invalid_post_response = requests.post(self.base_url, data = self.payload, headers = self.invalidheaders)
        return self.invalid_post_response
        
    
    def create_new_guser_without_authorization(self):
        self.not_authorized_user = requests.post(self.base_url, data = self.payload)
        return self.not_authorized_user

 
    def get_guser_with_not_existing_id(self):
        self.not_existing_user = requests.get(url=f'{BASE_URL}/{self.not_existing_id}', data = self.payload)
        return self.not_existing_user

 
    def create_guser_with_invalid_endpoint(self):
        self.invalid_user = requests.post(url= f'{BASE_URL}/{self.test}', data = self.payload, headers = self.header)
        return self.invalid_user
   
    def get_added_user(self):
        self.get_all_users = requests.get(self.base_url, headers = self.header).json()
        global added_user
        added_user = [self.person for self.person in self.get_all_users if self.person['name'] == self.unique_name][0]
        self.get_url = f'{BASE_URL}/{added_user["id"]}'
        self.get_response = requests.get(self.get_url, headers = self.header)
        return self.get_response.json()['name'], self.get_response.status_code

  
    def change_created_user(self):
        global person_id
        person_id = added_user['id']
        self.updated_url = f'{BASE_URL}/{person_id}'
        put_response = requests.put(self.updated_url, data = self.updated_payload, headers = self.header)
        return  person_id, put_response.status_code

    
    def delete_created_user(self):
        self.delete_url = f'{BASE_URL}/{person_id}'
        delete_response = requests.delete(self.delete_url, headers = self.header)
        return  delete_response.status_code


    