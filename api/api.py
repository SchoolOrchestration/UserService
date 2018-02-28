"""
API Based ViewSets
"""
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import authenticate
from api.serializers import UserSerializer
from api.schema import user_login_schema
from django.http import JsonResponse
from django.conf import settings
from .models import Organization
from api.serializers import (
    # OrganizationSerializer,
    UserLoginSerializer,
    UserLogin
)
# from rest_framework import (
#     permissions,
#     viewsets
# )
from rest_framework.decorators import (
    api_view,
    schema
)


# Create your views here.
@csrf_exempt
@api_view(['GET'])
def health(request):
    """
    A health endpoint that runs health checks on the db
    """
    def can_connect_to_dependencies():
        """
        Logic to check connection to dependencies
        TODO: Abstract health_check to library
        :return string{up|down}
        """
        # Will throw an exception if database cannot connect
        get_user_model().objects.first()

        response = {
            "status": "OK",
            "db": "OK",
            "queue": "Not Connected",
            "pub_sub": "Not Connected"
        }
        return response
    data = {
        'version': settings.VERSION,
        'status': {'dependencies': can_connect_to_dependencies()}}
    return JsonResponse(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@schema(user_login_schema)
def get_user_info(request):
    """
    This API returns a user object once authentication against a
    username and password.
    """
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
            serialized = UserSerializer(user)
            data = serialized.data
            status_code = 200
    return JsonResponse(data, status=status_code)


"""
Resource Viewsets
"""


# class OrganizationViewset(viewsets.ModelViewSet):
#     serializer_class = OrganizationSerializer
#     queryset = Organization.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)
