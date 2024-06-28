from rest_framework import serializers
from core.models.drivers import Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = ['id', 'name', 'vehicle_id', 'vehicle_type','phone_number','address']
