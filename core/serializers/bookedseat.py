from rest_framework import serializers

from core.models.bookedseats import BookedSeat


class BookedSeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookedSeat
        fields = ['id', 'seat_number']
