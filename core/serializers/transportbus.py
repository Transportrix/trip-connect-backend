from rest_framework import serializers

from core.models.transportbuses import TransportBus
from core.serializers.driver import DriverSerializer


class TransportBusSerializer(serializers.ModelSerializer):
    driver = DriverSerializer()

    class Meta:
        model = TransportBus
        fields = '__all__'
