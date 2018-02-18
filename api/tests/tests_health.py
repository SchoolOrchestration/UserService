from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse


# Create your tests here.
class HealthTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create_user("test_user")

    def test_health_endpoint_ok(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
