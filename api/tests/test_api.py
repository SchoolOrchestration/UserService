from rest_framework.test import APIClient as Client
from django.contrib.auth.models import User
from django.test import TestCase
import faker
import uuid


class UserTestCase(TestCase):

    def setUp(self):
        f = faker.Faker()
        self.password = str(uuid.uuid4())
        self.user = User.objects.create_user(
            username=f.first_name(),
            password=self.password
        )
        self.client = Client()

    def test_get_user(self):
        response = self.client.post(
            "/login",
            {
                'username': self.user.username,
                'password': self.password
            }
        )
        expected_response = {
            "username": self.user.username,
            "id": self.user.id
        }
        self.assertTrue(response.json() == expected_response,
                        msg='User not authenticated')

    def test_get_user_fails(self):
        response = self.client.post(
            "/login/",
            {
                'username': self.user.username,
                'password': str(uuid.uuid4())
            }
        )
        self.assertTrue(response.status_code == 401,
                        msg='Authentication failure not handled')
