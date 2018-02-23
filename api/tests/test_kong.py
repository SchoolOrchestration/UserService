from django.test import TestCase, override_settings
from django.conf import settings
from api.kong import Consumer
from faker import Faker
import responses
import uuid


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
class KongConsumerTestCase(TestCase):
    def setUp(self):
        self.f = Faker()

    @responses.activate
    def test_consumer_create(self):
        username = self.f.first_name()
        kong_id = str(uuid.uuid4())
        responses.add(
            responses.POST,
            '{}/consumers/'.format(settings.KONG_ADMIN_URL),
            json={
                'created_at': 1519279548000,
                'username': username,
                'id': kong_id
            },
            status=201
        )
        consumer = Consumer.create(username=username)
        self.assertTrue(consumer.username == username)
        self.assertTrue(consumer.kong_id == kong_id)
