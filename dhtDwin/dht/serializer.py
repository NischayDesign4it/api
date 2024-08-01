from rest_framework import serializers
from .models import temphum, Status


class TempHumSerializer(serializers.ModelSerializer):
    class Meta:
        model = temphum
        fields = ['temperature', 'humidity']


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['Status']
