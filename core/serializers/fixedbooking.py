from rest_framework import serializers
from core.models.bookedseats import BookedSeat
from core.models.fixedbookings import FixedBooking
from core.models.transportschedules import (
    TransportBusesAndSchedules,
    TransportSchedules,
)
from core.serializers.bookedseat import BookedSeatSerializer
from core.serializers.transportschedules import TransportSchedulesSerializer
from core.serializers.vehicle import TransportBusSerializer


class TransportBusesAndSchedulesSerialize2(serializers.ModelSerializer):
    transportbus = TransportBusSerializer()
    schedule = TransportSchedulesSerializer()

    class Meta:
        model = TransportBusesAndSchedules
        fields = ["transportbus", "schedule", "created_at", "updated_at"]


class BookingsSerializer(serializers.ModelSerializer):
    booked_bus_seats = BookedSeatSerializer(many=True)
    bus_and_schedule = TransportBusesAndSchedulesSerialize2()

    class Meta:
        model = FixedBooking
        fields = "__all__"
