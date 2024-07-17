from django.db import models
from core.models.drivers import Driver


class VehicleType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=255, blank=True)
    vehicle_number = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()

    model = models.ForeignKey(
        VehicleModel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vehicles",
    )

    type = models.ForeignKey(
        VehicleType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vehicles",
    )

    # driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} -> {self.model} -> {self.name}"
