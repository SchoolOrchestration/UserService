"""
These schemas are for the Function Based Views Until a time that Django
Rest Swagger supports them. Otherwise use the Auto generated Schemas
"""
from rest_framework.schemas import ManualSchema
import coreschema
import coreapi


user_login_schema = ManualSchema(
    description=("A JSON object containing a username and password "
                 "pair"),
    fields=[
        coreapi.Field(
            "body",
            required=True,
            location="body",
            schema=coreschema.Object(),
        ),
    ]
)
