from rest_framework import serializers
from core.models.fixedbookings import FixedBooking
from core.serializers.bookedseat import BookedSeatSerializer
from core.serializers.busschedule import BusScheduleSerializer

class BookingsSerializer(serializers.ModelSerializer):
    bus_schedule = BusScheduleSerializer()
    booked_bus_seats = BookedSeatSerializer(many=True, read_only=True)

    class Meta:
        model = FixedBooking
        fields = ['id', 'user', 'bus_schedule', 'booking_date', 'status', 'booked_bus_seats']
