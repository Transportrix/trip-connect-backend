# core/serializers/transportbusesandschedules.py

from rest_framework import serializers
from core.serializers.vehicle import TransportBusSerializer
from core.models.transportschedules import TransportBusesAndSchedules, TransportSchedules

class TransportSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportSchedules
        fields = "__all__"

class TransportBusesAndSchedulesSerializer(serializers.ModelSerializer):
    transportbus = TransportBusSerializer()
    # schedule = TransportSchedulesSerializer()

    class Meta:
        model = TransportBusesAndSchedules
        fields = ["transportbus", "created_at", "updated_at"]

class TransportSchedulesWithBusesSerializer(serializers.ModelSerializer):
    transportbusesandschedules_set = TransportBusesAndSchedulesSerializer(many=True, read_only=True)
    class Meta:
        model = TransportSchedules
        fields = [
            "id",
            "travelling_from",
            "travelling_to",
            "departure_time",
            "estimated_arrival_time",
            "transportbusesandschedules_set",
            "created_at",
            "updated_at",
        ]
