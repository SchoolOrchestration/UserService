from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from django.conf import settings
from faker import Faker
from ..models import (
    Organization,
    Profile,
    Team,
)
import responses
import uuid


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
class UserModelRelationshipTestCase(TestCase):

    @responses.activate
    def setUp(self):
        f = Faker()
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
        self.user_one = User.objects.create_user(username='user_one')
        self.team_one = Team.objects.create(name='team_one',
                                            organization=self.org)
        self.team_two = Team.objects.create(name='team_two',
                                            organization=self.org)

    def test_create_profile(self):
        Profile.objects.create(user=self.user_one,
                               team=self.team_one)
        Profile.objects.create(user=self.user_one,
                               team=self.team_two)
        self.assertTrue(self.user_one.team_set.all().count() == 2,
                        msg="User >--< Team relationship not defined")


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
class OrganizationModelTestCase(TestCase):

    @responses.activate
    def setUp(self):
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

    def test_check_organization_created_with_signals(self):
        self.assertTrue(Organization.objects.all().count() == 1,
                        msg="Organization not created")
        self.assertTrue(Team.objects.all().count() == 1,
                        msg="Team not created")
        self.assertTrue(Profile.objects.all().count() == 1,
                        msg="Profile not created")
        self.assertTrue(User.objects.all().count() == 1,
                        msg="User not created")
