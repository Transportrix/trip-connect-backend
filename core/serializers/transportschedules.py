# core/serializers/transportbusesandschedules.py

from rest_framework import serializers
from core.serializers.vehicle import VehicleSerializer
from core.models.transportschedules import (
    TransportBusesAndSchedules,
    TransportSchedules,
)


class TransportBusesAndSchedulesSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = TransportBusesAndSchedules
        fields = ["vehicle", "created_at", "updated_at"]


# core/serializers/transportschedules.py


class TransportSchedulesSerializer(serializers.ModelSerializer):
    transportbusesandschedules_set = TransportBusesAndSchedulesSerializer(
        many=True, read_only=True
    )

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
