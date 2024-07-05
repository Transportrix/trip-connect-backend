from django.db import models

from core.models.transportbuses import TransportBus


class BusSchedule(models.Model):
    bus = models.ForeignKey(TransportBus, on_delete=models.CASCADE)
    travelling_from = models.CharField(max_length=255)
    travelling_to = models.CharField(max_length=255)
    departure_time = models.DateTimeField()
    estimated_arrival_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.travelling_from} to {self.travelling_to}"