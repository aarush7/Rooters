from user_roles.models import attendant
from rest_framework import serializers


class AttendantEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendant
        exclude = ['attendant_id']


class AttendantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = attendant
        fields = '__all__'

