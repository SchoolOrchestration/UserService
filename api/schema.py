from rest_framework.schemas import ManualSchema
import coreapi
import uuid

user_login_schema = ManualSchema(
    fields=[
        coreapi.Field(
            "body",
            required=True,
            location="body",
            schema={
                'username': 'test_user',
                'password': str(uuid.uuid4())
            }
        ),
    ]
)
