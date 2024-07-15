from rest_framework import serializers

from core.models.fixedbookings import FixedBooking
from core.models.transportbus import TransportBus
from core.models.vehicles import Vehicle
from core.serializers.driver import DriverSerializer


class VehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicle_number', 'capacity', 'model']



class TransportBusSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    booked_seats_count = serializers.SerializerMethodField()

    class Meta:
        model = TransportBus
        fields = ['id', 'booked_seats_count', 'vehicle', 'bus_type']

    def get_booked_seats_count(self, obj):
        # Query FixedBooking instances related to this TransportBus
        bookings = FixedBooking.objects.filter(bus_and_schedule__transportbus=obj)
        # Calculate total booked seats across all related bookings
        total_booked_seats = sum(booking.booked_bus_seats.count() for booking in bookings)
        return total_booked_seats