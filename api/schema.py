"""
These schemas are for the Function Based Views Until a time that Django
Rest Swagger supports them. Otherwise use the Auto generated Schemas
"""
from rest_framework.schemas import ManualSchema
import coreapi
import uuid

user_login_schema = ManualSchema(
    fields=[
        coreapi.Field(
            "body",
            required=True,
            location="body",
            type="string",
            schema={
                'username': 'test_user',
                'password': str(uuid.uuid4())
            },
            description=("A JSON object containing a username and password "
                         "pair")
        ),
    ]
)
