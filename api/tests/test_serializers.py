from api.serializers import UserLoginSerializer
from django.test import TestCase
import faker
import uuid


class UserLoginSerializerTestCase(TestCase):
    def setUp(self):
        f = faker.Faker()
        self.data = {
            'username': f.first_name(),
            'password': str(uuid.uuid4())
        }

    def test_serialized_data(self):
        user = UserLoginSerializer(self.data).data
        self.assertTrue(user == self.data,
                        msg='User not serialized')
