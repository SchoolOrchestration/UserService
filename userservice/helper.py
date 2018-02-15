from django.conf import settings
import requests
import json
import os


def get_secret(secret_name, default=None):
    """Returns a docker secret"""
    try:
        return open('/run/secrets/{}'.format(secret_name)).read().rstrip()
    except FileNotFoundError:
        return os.environ.get(secret_name, default)
