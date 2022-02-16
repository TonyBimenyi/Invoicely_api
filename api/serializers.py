from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *
from django.db import transaction
from django.contrib.auth.models import Group
from rest_framework.response import Response
from django.contrib.auth.models import User


class TokenPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		data = super(TokenPairSerializer, self).validate(attrs)
		data['groups'] = [group.name for group in self.user.groups.all()]
		data['username'] = self.user.username
		data['id'] = self.user.id
		data['first_name'] = self.user.first_name
		data['last_name'] = self.user.last_name
		return data

class GroupSerializer(serializers.ModelSerializer):

	class Meta:
		model = Group
		fields = "__all__"


class ProviderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provider
		fields = "__all__"

class AbakiriyaSerializer(serializers.ModelSerializer):
	class Meta:
		model = abakiriya
		fields = "__all__"

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		representation["created_by"]=instance.created_by.username
		return representation