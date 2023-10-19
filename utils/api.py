import logging
import os
import requests

ENDPOINTS = {
    'SIGNUP': '/signup',
    'LOGIN': '/login'
}


def make_request(method, url, **kwargs):
    logging.info(f'making a {method} request to endpoint {url}')
    return requests.request(method, url, **kwargs)


def get_url(endpoint):
    return os.getenv('BASE_URL') + endpoint

