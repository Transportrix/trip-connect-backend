from rest_framework import serializers

from core.models.bookedseats import BookedSeat
from core.models.fixedbookings import FixedBooking
from core.models.transportbus import TransportBus
from core.models.vehicleimage import VehicleImage
from core.models.vehicles import Vehicle, VehicleModel, VehicleType
from core.serializers.bookedseat import BookedSeatSerializer
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
    booked_seats = serializers.SerializerMethodField()

    class Meta:
        model = TransportBus
        fields = ["id", "booked_seats", "vehicle", "bus_type"]

    def get_booked_seats(self, obj):
        booked_seats = BookedSeat.objects.filter(booking__bus_and_schedule__transportbus=obj)
        return BookedSeatSerializer(booked_seats, many=True).data
