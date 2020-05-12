from user_roles.models import bankinfo
from rest_framework import serializers


class BankinfoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = bankinfo
        exclude = ['user_id']


class BankinfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = bankinfo
        fields = '__all__'

