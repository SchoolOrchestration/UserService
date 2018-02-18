"""
These schemas are for the Function Based Views Until a time that Django
Rest Swagger supports them. Otherwise use the Auto generated Schemas
"""
# encoding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_swagger import renderers
from django.utils.module_loading import import_string
import coreapi

user_login_schema = coreapi.Document(
    title='User Login',
    url='/users/',
    content={
        'Login': coreapi.Link(
            url='/login/',
            action='Post',
            fields=[
                coreapi.Field(
                    name='body',
                    required=True,
                    location='body',
                    description='Returns a User Object on Authentication'
                ),
            ],
            description='Authenticate users'
        ),
        'Health': coreapi.Link(
            url='/health/',
            action='Get',
            description='Health Endpoint'
        )
    }
)


def get_swagger_view(schema_location):
    """
    Returns schema view which renders Swagger/OpenAPI.
    """
    class SwaggerSchemaView(APIView):
        _ignore_model_permissions = True
        exclude_from_schema = True
        permission_classes = [AllowAny]
        renderer_classes = [
            CoreJSONRenderer,
            renderers.OpenAPIRenderer,
            renderers.SwaggerUIRenderer
        ]

        def get(self, request):
            schema = None

            try:
                schema = import_string(schema_location)
            except:
                pass

            if not schema:
                raise exceptions.ValidationError(
                    'The schema generator did not return a schema Document'
                )

            return Response(schema)


    return SwaggerSchemaView.as_view()

