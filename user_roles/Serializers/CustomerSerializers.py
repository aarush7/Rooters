from user_roles.models import customer
from rest_framework import serializers


class CustomerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        exclude = ['customer_id']


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

