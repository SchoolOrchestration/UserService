from rest_framework import schemas
import coreapi
import coreschema


user_login_schema = schemas.AutoSchema(manual_fields=[
    coreapi.Field(
        "body",
        required=True,
        location="body",
        schema=coreschema.Object(),
        description="Returns a user object after authenticating",
        example="",
    ),
])
