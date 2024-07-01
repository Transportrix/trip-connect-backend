from rest_framework import serializers
from core.models.bookings import Booking

class BookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'pickup_time', 'distance', 'fare', 'destination']
