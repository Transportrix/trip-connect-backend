
from rest_framework import serializers

from core.models.busschedules import BusSchedule

class BusScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = '__all__'

