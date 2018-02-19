from rest_framework import schemas
import coreapi
import coreschema


user_login_schema = schemas.ManualSchema(fields=[
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
])
