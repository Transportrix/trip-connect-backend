from django.db import models
from core.models.vehicles import Vehicle

class TransportBus(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    bus_type = models.CharField(max_length=255)  # e.g., "Luxury", "Economy", etc.
    additional_features = models.TextField(null=True, blank=True)  # Any additional features or details about the bus

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transport Bus {self.vehicle.vehicle_number} - Type: {self.bus_type}"
