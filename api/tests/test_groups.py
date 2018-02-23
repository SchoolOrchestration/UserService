from django.test import TestCase, override_settings
from django.contrib.auth.models import Group


@override_settings(KONG_ADMIN_URL="https://kong-staging.vumatel.co.za/manage")
class GroupTestCase(TestCase):
    def setUp(self):
        self.group_name = 'organisation.perm_one.perm_two'

    def test_create_group(self):
        Group.objects.get_or_create(name=self.group_name)
        self.assertTrue(Group.objects.all().count() == 1,
                        msg='Group Not Created')
