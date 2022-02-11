from posixpath import basename
from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('providers', ProviderView, basename='provider')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),

]