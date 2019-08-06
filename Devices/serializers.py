__author__ = 'Da Vinci'
from rest_framework import serializers
from Devices.models import Devices

class DevicesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'device_name',
            'device_slug',
            'token_value',
            'device_status',
            'longitude',
            'latitude',)
        model = Devices