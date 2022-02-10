from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import transaction
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework import viewsets

from .serializers import *
from .models import *

class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer

class GroupViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = IsAuthenticated,
    queryset = Group.objects.all()
    serializer_class = GroupSerializer