from datetime import datetime
import pytest
import datetime
from modules import users


def pytest_configure(config):
    config.option.htmlpath = f'reports\\report-{datetime.datetime.now().strftime("%f")}.html'


@pytest.fixture(scope="session")
def setup_signup():
    yield users.signup_with_random_username()
