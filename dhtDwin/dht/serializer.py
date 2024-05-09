from rest_framework import serializers
from .models import temphum


class TempHumSerializer(serializers.ModelSerializer):
    class Meta:
        model = temphum
        fields = ['temperature', 'humidity']
