from user_roles.models import operator
from rest_framework import serializers


class OperatorEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = operator
        exclude = ['operator_id']


class OperatorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = operator
        fields = '__all__'

