import pytest
from modules import users
from test_data import users_test_data
from utils import data_generator, api


class TestLogin:

    @pytest.mark.login
    @pytest.mark.parametrize('username,password, exp_status_code, expected_msg', users_test_data.LOGIN_TEST_DATA)
    def test_login(self, username, password, exp_status_code, expected_msg):
        response = users.login_with(username, password)
        assert response.status_code == exp_status_code
        assert expected_msg in str(response.json())

    @pytest.mark.parametrize('method', users_test_data.INVALID_API_METHODS)
    def test_login_api_with_invalid_methods(self, method):
        username, password = data_generator.generate_user_creds()
        creds = users.create_user_json(username, password)
        response = api.make_request(method, api.get_url(api.ENDPOINTS['LOGIN']), json=creds)
        assert response.status_code == 405

