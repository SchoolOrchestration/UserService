from django.conf.urls import url, include
from rest_framework import routers
from api.api import *

router = routers.DefaultRouter()
router.register(prefix=r'health', viewset=HealthViewSet, base_name='health')
router.register(prefix=r'user', viewset=UserViewSet, base_name='user')

urlpatterns = [
    url(r'^', include(router.urls), name="api")
]
