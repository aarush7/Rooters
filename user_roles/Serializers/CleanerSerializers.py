from user_roles.models import cleaner
from rest_framework import serializers


class CleanerEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = cleaner
        exclude = ['cleaner_id']


class CleanerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = cleaner
        fields = '__all__'

