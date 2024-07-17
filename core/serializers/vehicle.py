from rest_framework import serializers

from core.models.fixedbookings import FixedBooking
from core.models.transportbus import TransportBus
from core.models.vehicleimage import VehicleImage
from core.models.vehicles import Vehicle, VehicleModel, VehicleType
from core.serializers.driver import DriverSerializer


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ["name"]


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ["name"]


class VehicleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleImage
        fields = ("image",)  # Assuming you want to include only the image field


class VehicleSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    model = VehicleModelSerializer()
    type = VehicleTypeSerializer()

    class Meta:
        model = Vehicle
        fields = ["id", "name", "vehicle_number", "capacity", "model", "type", "images"]

    def get_images(self, obj):
        vehicle_images = VehicleImage.objects.filter(vehicle=obj)
        return VehicleImageSerializer(
            vehicle_images, many=True, context=self.context
        ).data


class TransportBusSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    booked_seats_count = serializers.SerializerMethodField()

    class Meta:
        model = TransportBus
        fields = ["id", "booked_seats_count", "vehicle", "bus_type"]

    def get_booked_seats_count(self, obj):
        # Query FixedBooking instances related to this TransportBus
        bookings = FixedBooking.objects.filter(bus_and_schedule__transportbus=obj)
        # Calculate total booked seats across all related bookings
        total_booked_seats = sum(
            booking.booked_bus_seats.count() for booking in bookings
        )
        return total_booked_seats
