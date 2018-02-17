from rest_framework.schemas import ManualSchema
import coreschema
import coreapi

user_login_schema = ManualSchema(
    fields=[
        coreapi.Field(
            "username",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
        coreapi.Field(
            "password",
            required=True,
            location="form",
            schema=coreschema.String()
        ),
    ]
)
