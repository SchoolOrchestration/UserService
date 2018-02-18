"""
API Based ViewSets
"""
from api.serializers import UserLoginSerializer, UserLogin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .schema import user_login_schema
from django.http import JsonResponse
from django.conf import settings
from rest_framework_swagger.renderers import (
    SwaggerUIRenderer,
    OpenAPIRenderer
)
from rest_framework import (
    decorators,
    viewsets,
    status
)


# Create your views here.
class HealthViewSet(viewsets.ViewSet):

    @classmethod
    def list(cls, request):
        """Health Endpoint"""
        data = {'status': {'db': cls.can_connect_to_db()}}
        return Response(data, status=status.HTTP_200_OK)

    @staticmethod
    def can_connect_to_db():
        """
        Logic to check connection to db
        :return string{up|down}
        """
        # Will throw an exception if database cannot connect
        get_user_model().objects.first()

        response = {
            "status": "OK",
            "db": "OK",
            "version": settings.VERSION
        }
        return response


@csrf_exempt
@decorators.api_view(['POST'])
@decorators.schema(user_login_schema)
@decorators.renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def get_user_info(request):
    serialized_data = UserLoginSerializer(data=request.data)
    status_code = 401
    data = dict()
    if serialized_data.is_valid():
        user_login = UserLogin()
        user_login.username = serialized_data.data['username']
        user_login.password = serialized_data.data['password']
        user = authenticate(
            username=user_login.username,
            password=user_login.password
        )
        if user:
            data['username'] = user.username
            data['id'] = user.id
            status_code = 200
    return JsonResponse(data, status=status_code)
