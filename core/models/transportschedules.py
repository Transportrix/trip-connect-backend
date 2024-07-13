from django.db import models

from core.models.vehicles import Vehicle


class TransportSchedules(models.Model):
    travelling_from = models.CharField(max_length=255)
    travelling_to = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.travelling_from} to {self.travelling_to}"


class TransportBusesAndSchedules(models.Model):
    schedule = models.ForeignKey(TransportSchedules, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Schedule {self.schedule.id} - Vehicle {self.vehicle.vehicle_number}"
