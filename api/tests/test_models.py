from django.test import TestCase, override_settings
from django.conf import settings
from ..models import (
    Organization,
)
import responses
import uuid


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
@override_settings(KONG_MANAGER_TOKEN="123456789")
class OrganizationModelTestCase(TestCase):

    @responses.activate
    def setUp(self):
        kong_id = str(uuid.uuid4())
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

    def test_check_organization_created_with_signals(self):
        self.assertTrue(Organization.objects.all().count() == 1,
                        msg="Organization not created")
