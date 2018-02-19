"""
API Based ViewSets
"""
from api.serializers import UserLoginSerializer, UserLogin
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.status import HTTP_200_OK
from django.contrib.auth import authenticate
from api.schema import user_login_schema
from django.http import JsonResponse
from django.conf import settings
from rest_framework.decorators import (
    api_view,
    schema
)


# Create your views here.
@csrf_exempt
@api_view(['GET'])
def health(request):
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
    description: This API deletes/uninstalls a device.
    parameters:
      - name: name
        type: string
        required: true
        location: form
      - name: bloodgroup
        type: string
        required: true
        location: form
      - name: birthmark
        type: string
        required: true
        location: form
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
            data['username'] = user.username
            data['id'] = user.id
            status_code = 200
    return JsonResponse(data, status=status_code)
