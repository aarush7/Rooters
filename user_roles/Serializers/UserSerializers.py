from user_roles.models import user
from rest_framework import serializers


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        exclude = ['user_id']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'

