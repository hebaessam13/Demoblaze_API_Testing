import logging
import os
import requests
from dotenv import load_dotenv

ENDPOINTS = {
    'SIGNUP': '/signup',
    'LOGIN': '/login'
}

def make_request(method, url, **kwargs):
    logging.info(f'making a {method} request to endpoint {url}')
    return requests.request(method, url, **kwargs)


def get_url(endpoint):
    load_dotenv()
    return os.environ.get('BASE_URL') + endpoint

