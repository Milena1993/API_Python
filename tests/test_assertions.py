from calls.requests import APIRequests
from calls.data import Testdata
from config import API_TOKEN, BASE_URL
from assertpy.assertpy import assert_that
from urllib import response
import requests
import pytest
import json


class Tests(Testdata):

    # Get all users added by me
    def test_get_all_data(self):
        get_data = APIRequests()
        get_response = get_data.get_all_data()
        assert_that(get_response.status_code).is_equal_to(requests.codes.ok)

    # 201 status code-user is created
    def test_new_user_successfully_created(self):
        get_data = APIRequests()
        new_user = get_data.create_new_guser()
        assert_that(new_user).is_equal_to(
            (self.unique_name, requests.codes.created))

    # 422 status code: Data validation failed
    def test_invalid_guser_422_code(self):
        get_data = APIRequests()
        invalid_user = get_data.create_new_guser_with_invalid_data()
        assert_that(invalid_user.status_code).is_equal_to(
            requests.codes.unprocessable_entity)

    # 401 status code: Authentication failed.
    def test_invalid_guser_401_code(self):
        get_data = APIRequests()
        unauthorized_user = get_data.create_new_guser_without_authorization()
        assert_that(unauthorized_user.status_code).is_equal_to(
            requests.codes.unauthorized)

    # 404 status code:  Not found
    def test_invalid_guser_404_code(self):
        get_data = APIRequests()
        not_existing_user = get_data.get_guser_with_not_existing_id()
        assert_that(not_existing_user.status_code).is_equal_to(
            requests.codes.not_found)

    # 400 status code: Bad Request
    def test_invalid_guser_400_code(self):
        get_data = APIRequests()
        invalid_user = get_data.create_guser_with_invalid_endpoint()
        assert_that(invalid_user.status_code).is_equal_to(
            requests.codes.bad_request)

    # 200 status code-everything worked as expected

    def test_get_added_user(self):
        get_data = APIRequests()
        get_added_user = get_data.get_added_user()
        assert_that(get_added_user).is_equal_to(
            (self.unique_name, requests.codes.ok))

    # Put request-data successfully changed
    def test_update_user(self):
        get_data = APIRequests()
        get_updated_user = get_data.change_created_user()
        assert_that(get_updated_user).contains(requests.codes.ok)

    # 204 status code_User is deleted
    def test_delete_created_user(self):
        get_data = APIRequests()
        get_deleted_user = get_data.delete_created_user()
        assert_that(get_deleted_user).is_equal_to(requests.codes.no_content)
