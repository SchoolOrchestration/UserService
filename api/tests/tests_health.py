from rest_framework.test import APIClient
from api.api import HealthViewSet
from django.test import TestCase
from unittest.mock import patch
from django.urls import reverse


# Create your tests here.
class HealthTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch.object(HealthViewSet, 'can_connect_to_db')
    def test_health_endpoint_ok(self, mock_one):
        mock_one.return_value = 'up'
        url = reverse('health-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
