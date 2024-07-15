# serializers.py
from rest_framework import serializers

from core.models.flexiblebookings import FlexibleBooking

class FlexibleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlexibleBooking
        fields = '__all__'