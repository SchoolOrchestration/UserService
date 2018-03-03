from rest_framework.test import APIClient as Client
from django.test import TestCase, override_settings
from django.test.client import RequestFactory
from django.conf import settings
import redis
import json


class AuthenticationClassKongOAuthTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.headers = {
            'HTTP_X_ANONYMOUS_CONSUMER': False,
            'HTTP_X_AUTHENTICATED-USERID': 3
        }
        self.user_data = {
            'username': 'Natalie',
            'id': 3,
            'organizations': [
                {
                    'name': 'Organization',
                    'id': 3,
                    'groups': [
                        {
                            'name': 'organization.admin',
                            'permissions': [
                                {'name': 'all', 'code': 'all'}
                            ]
                        }
                    ]
                }
            ]
        }
        redis.StrictRedis(settings.PERMISSIONS_HOST).set('authorization.3',
                                                         json.dumps(self.user_data))

    def test_middleware_gets_called(self):
        response = self.client.get(
            '/oauth/test/',
            **self.headers
        )
