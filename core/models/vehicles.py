from django.db import models

from core.models.drivers import Driver
# Create your models here.

class Vehicle(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    licence_plate_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    # vehicle_type = models.TextChoices("STC", "VIP")
    brand = models.TextField(max_length=50)
