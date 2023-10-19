import logging
from utils import data_generator, api


def signup_with(username, password):
    user_creds = create_user_json(username, password)
    logging.info(f'Creating account for user : {username}')
    return api.make_request('POST', api.get_url(api.ENDPOINTS['SIGNUP']), json=user_creds)


def login_with(username, password):
    user_creds = create_user_json(username, password)
    logging.info(f'logining with user : {username}')
    return api.make_request('POST', api.get_url(api.ENDPOINTS['LOGIN']), json=user_creds)


def signup_with_random_username():
    username = data_generator.generate_string(8)
    password = data_generator.generate_string(10)
    response = signup_with(username, password)
    assert 'error' not in str(response.json())
    return username, password


def create_user_json(username, password):
    return {'username': username, 'password': password}
