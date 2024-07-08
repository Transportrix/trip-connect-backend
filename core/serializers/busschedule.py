
from rest_framework import serializers

from core.models.busschedules import BusSchedule
from core.serializers.transportbus import TransportBusSerializer

class BusScheduleSerializer(serializers.ModelSerializer):
    bus = TransportBusSerializer()
    class Meta:
        model = BusSchedule
        fields = '__all__'

