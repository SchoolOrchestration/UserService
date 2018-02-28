from rest_framework.test import APIClient as Client
from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from django.conf import settings
from ..models import (
    TeamPermissions,
    Organization,
    Permission,
    Team,
)
import responses
import faker
import uuid


# @override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
# @override_settings(KONG_MANAGER_TOKEN="123456789")
# class OrganizationApiTestCase(TestCase):
#
#     def setUp(self):
#         self.client = Client()
#
#     @responses.activate
#     def test_create_organization(self):
#         kong_id = str(uuid.uuid4())
#         responses.add(
#             responses.POST,
#             '{}/consumers/?apikey={}'.format(settings.KONG_ADMIN_URL,
#                                              settings.KONG_MANAGER_TOKEN),
#             json={
#                 'created_at': 1519279548000,
#                 'username': 'organization_admin',
#                 'id': kong_id
#             },
#             status=201
#         )
#         response = self.client.post(
#             "/organization/",
#             {"name": "Organization"}
#         )
#         import ipdb;ipdb.set_trace()
#         self.assertTrue(response.status_code == 201,
#                         msg="Organization API create not working")


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
@override_settings(KONG_MANAGER_TOKEN="123456789")
class UserTestCase(TestCase):

    @responses.activate
    def setUp(self):
        f = faker.Faker()
        kong_id = str(uuid.uuid4())
        self.password = str(uuid.uuid4())
        responses.add(
            responses.POST,
            '{}/consumers/?apikey={}'.format(settings.KONG_ADMIN_URL,
                                             settings.KONG_MANAGER_TOKEN),
            json={
                'created_at': 1519279548000,
                'username': 'organization_admin',
                'id': kong_id
            },
            status=201
        )
        self.org = Organization.objects.create(name='Organization')
        self.perm = Permission.objects.create(name='all', code='code')
        self.user = User.objects.create_user(
            username=f.first_name(),
            password=self.password
        )
        self.user.organization_set.add(self.org)
        self.team = Team.objects.create(
            name="{}.admin".format(self.org.name.lower()),
            organization=self.org,
        )
        self.user.team_set.add(self.team)
        self.team_perm = TeamPermissions.objects.create(permission=self.perm,
                                                        team=self.team)
        self.client = Client()
        self.response = self.client.post(
            "/login/",
            {
                'username': self.user.username,
                'password': self.password
            }
        )

    def test_get_user_id(self):
        self.assertTrue(self.response.json()['id'] == self.user.id,
                        msg='User Id Not in response')

    def test_get_user_org(self):
        self.assertTrue(self.response.json()['organizations'] is not None,
                        msg='Organizations not in response')

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
