import os
import pytest
from api_helpers.auth_helper import AuthHelper


def test_successful_login():
    auth = AuthHelper()
    email = os.getenv('USER_EMAIL')
    password = os.getenv("USER_PASSWORD")

    token = auth.login(email,password)

    assert token is not None
    assert len(token) > 10