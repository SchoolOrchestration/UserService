from rest_framework.test import APIClient as Client
from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from django.conf import settings
from ..models import (
    Organization,
    Profile,
    Team,
)
import responses
import faker
import uuid


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
class UserTestCase(TestCase):
    @responses.activate
    def setUp(self):

        f = faker.Faker()
        kong_id = str(uuid.uuid4())
        responses.add(
            responses.POST,
            '{}/consumers/'.format(settings.KONG_ADMIN_URL),
            json={
                'created_at': 1519279548000,
                'username': 'organization_admin',
                'id': kong_id
            },
            status=201
        )
        self.org = Organization.objects.create(name='Organization')
        self.team_one = Team.objects.create(name='team_one',
                                            organization=self.org)
        self.team_two = Team.objects.create(name='team_two',
                                            organization=self.org)
        self.password = str(uuid.uuid4())
        self.user = User.objects.create_user(
            username=f.first_name(),
            password=self.password
        )
        Profile.objects.create(user=self.user,
                               team=self.team_one)
        Profile.objects.create(user=self.user,
                               team=self.team_two)
        self.client = Client()

    def test_get_user(self):
        response = self.client.post(
            "/login/",
            {
                'username': self.user.username,
                'password': self.password
            }
        )
        expected_response = {
            "username": self.user.username,
            "id": self.user.id,
            "organization": self.org.name,
            "teams": [self.team_one.name, self.team_two.name]
        }
        import ipdb;ipdb.set_trace()
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
