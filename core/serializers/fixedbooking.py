from rest_framework import serializers
from core.models.fixedbookings import FixedBooking

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedBooking
        fields = ['id', 'user', 'bus_schedule', 'booking_date', 'status']
