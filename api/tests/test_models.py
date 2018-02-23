from django.contrib.auth.models import User
from django.test import TestCase
from faker import Faker
from ..models import (
    Organization,
    Profile,
    Team,
)


class UserModelRelationshipTestCase(TestCase):

    def setUp(self):
        f = Faker()
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
