from django.db import router
from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenPairView.as_view()),

]