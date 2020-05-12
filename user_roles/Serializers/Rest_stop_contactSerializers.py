from user_roles.models import rest_stop_contact
from rest_framework import serializers


class Rest_stop_contactEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = rest_stop_contact
        exclude = ['rest_stop_contact_id']


class Rest_stop_contactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = rest_stop_contact
        fields = '__all__'

