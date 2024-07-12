from rest_framework import serializers
from core.models.bookedseats import BookedSeat
from core.models.fixedbookings import FixedBooking
from core.models.transportschedules import TransportSchedules
from core.serializers.bookedseat import BookedSeatSerializer
from core.serializers.transportschedules import TransportSchedulesSerializer


class BookingsSerializer(serializers.ModelSerializer):
    booked_bus_seats = BookedSeatSerializer(many=True)
    bus_schedule = TransportSchedulesSerializer()

    class Meta:
        model = FixedBooking
        fields = "__all__"
