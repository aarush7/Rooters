from user_roles.models import driver
from rest_framework import serializers


class DriverEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver
        exclude = ['driver_id']


class DriverListSerializer(serializers.ModelSerializer):
    class Meta:
        model = driver
        fields = '__all__'

