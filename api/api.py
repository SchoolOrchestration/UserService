from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.conf import settings
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
def get_user_info(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    user = authenticate(username=username, password=password)
    data = dict()
    status_code = 401
    if user:
        data['username'] = user.username
        data['id'] = user.id
        status_code = 200
    return JsonResponse(data, status=status_code)
