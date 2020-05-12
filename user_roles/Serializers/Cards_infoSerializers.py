from user_roles.models import cards_info
from rest_framework import serializers


class Cards_infoEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = cards_info
        exclude = ['card_info_id']


class Cards_infoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = cards_info
        fields = '__all__'

