from rest_framework import serializers

from core.models.vehicles import Vehicle
from core.serializers.driver import DriverSerializer


class VehicleSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()
    
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_number', 'capacity', 'model', 'driver']
