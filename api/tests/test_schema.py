
from rest_framework.test import APIClient as Client
from django.test import TestCase
from django.urls import reverse


class UserLoginSchemaTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("docs")

    def test_schema_call(self):
        pass
