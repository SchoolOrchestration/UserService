"""
These Schema should be for FBV(Function Based Views) only as swagger UI
and django rest framework schemas do not fully support schemas for FBV
"""
from rest_framework import schemas
import coreapi
import coreschema


user_login_schema = schemas.ManualSchema(
    description="""
    **User Validation**: This API returns a user object once 
    authentication against a username and password.
    """,
    fields=[
        coreapi.Field(
            "username",
            required=True,
            location="form",
            schema=coreschema.String(),
            example="test_user",
        ),
        coreapi.Field(
            "password",
            required=True,
            location="form",
            schema=coreschema.String(),
            example="test_password",
        )
    ]
)
