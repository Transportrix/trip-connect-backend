
from rest_framework import serializers

from core.models.transportschedules import TransportSchedules
from core.serializers.vehicle import VehicleSerializer

class TransportSchedulesSerializer(serializers.ModelSerializer):
    bus = VehicleSerializer()
    class Meta:
        model = TransportSchedules
        fields = '__all__'

