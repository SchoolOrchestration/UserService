from rest_framework.test import APIClient as Client
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
import faker
import uuid


class UserTestCase(TestCase):

    def setUp(self):
        self.faker = faker.Faker()
        User.objects.create_user(
            username=self.faker.first_name(),
            password=str(uuid.uuid4())
        )
        self.client = Client()

    def test_list_user(self):
        response = self.client.get("/user/")
        self.assertTrue(len(response.json()) == 1,
                        msg='User ViewSet working')
