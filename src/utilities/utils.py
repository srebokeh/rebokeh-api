from base64 import b64encode
import requests
from django.utils import timezone
from django.utils.crypto import get_random_string
from datetime import timedelta
import datetime
from django.conf import settings

import jwt




def generate_access_token(user_id):
    """
    Generate an access token for the given user ID.

    """

    access_token_payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now() + datetime.timedelta(days=365),
        'iat': datetime.datetime.now(),
    }
    access_token = jwt.encode(access_token_payload,settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return access_token



def generate_refresh_token(user_id):
    """
    Generate a refresh token for the given user ID.

    """
    refresh_token_payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now() + datetime.timedelta(days=7),
        'iat': datetime.datetime.now()
    }
    refresh_token = jwt.encode(refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm=settings.JWT_ALGORITHM)
    return refresh_token


