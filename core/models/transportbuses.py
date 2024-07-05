from django.db import models

from core.models.drivers import Driver


class TransportBus(models.Model):
    bus_number = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    model = models.CharField(max_length=255, null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bus_number