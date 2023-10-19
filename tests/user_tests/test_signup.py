import pytest
from modules import users
from test_data import users_test_data
from utils import data_generator, api


class TestSignUp:

    @pytest.mark.signup
    @pytest.mark.parametrize('username,password, exp_status_code, expected_msg', users_test_data.SIGNUP_TEST_DATA)
    def test_signup(self, username, password, exp_status_code, expected_msg):
        response = users.signup_with(username, password)
        assert response.status_code == exp_status_code
        assert expected_msg is str(response.json())

    @pytest.mark.parametrize('method', users_test_data.INVALID_API_METHODS)
    def test_signup_api_with_invalid_methods(self, method):
        username, password = data_generator.generate_user_creds()
        creds = users.create_user_json(username, password)
        response = api.make_request(method, api.get_url(api.ENDPOINTS['SIGNUP']), json=creds)
        assert response.status_code == 405
