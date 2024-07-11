from rest_framework import serializers
from core.models.transportschedules import TransportSchedules
from core.models.transportschedules import TransportBusesAndSchedules
from core.serializers.vehicle import VehicleSerializer


class TransportSchedulesSerializer(serializers.ModelSerializer):
    vehicles = serializers.SerializerMethodField()

    class Meta:
        model = TransportSchedules
        fields = '__all__'

    def get_vehicles(self, obj):
        # Get all TransportBusesAndSchedules related to this schedule
        transport_buses_and_schedules = obj.transportbusesandschedules_set.all()
        return TransportBusesAndSchedulesSerializer(transport_buses_and_schedules, many=True).data


class TransportBusesAndSchedulesSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()
    
    class Meta:
        model = TransportBusesAndSchedules
        fields = '__all__'
