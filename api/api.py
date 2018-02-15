from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.conf import settings


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
