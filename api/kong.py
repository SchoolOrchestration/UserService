from django.conf import settings
import requests


class Consumer:
    def __init__(self, username=None, kong_id=None):
        self.username = username
        self.kong_id = kong_id

    @classmethod
    def create(cls, username):
        cls.username = username
        response = requests.post(
            '{}/consumers/'.format(settings.KONG_ADMIN_URL),
            data={
                'username': cls.username
            }
        )
        if response.status_code == 201:
            cls.kong_id = response.json()['id']
            return cls
