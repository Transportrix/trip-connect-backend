# serializers.py
from rest_framework import serializers

from core.models.flexiblebookings import FlexibleBooking
from core.serializers.vehicle import VehicleSerializer

class FlexibleBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlexibleBooking
        fields = '__all__'

class FlexibleBookingDetailsSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    class Meta:
        model = FlexibleBooking
        fields = '__all__'