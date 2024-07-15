from django.db import models
from core.models.drivers import Driver

class Vehicle(models.Model):
    # Defining choices for vehicle type
    SEDAN = 'Sedan'
    TRUCK = 'Truck'
    SUV = 'SUV'
    VEHICLE_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (TRUCK, 'Truck'),
        (SUV, 'SUV'),
    ]

    # Defining choices for vehicle model (these are examples, you can add more)
    TOYOTA = 'Toyota'
    AUDI = 'Audi'
    FORD = 'Ford'
    BMW = 'BMW'
    PORSCHE = 'Porsche'
    ROLLS_ROYCE = 'Rolls Royce'

    VEHICLE_MODEL_CHOICES = [
        (TOYOTA, 'Toyota'),
        (AUDI, 'Audi'),
        (FORD, 'Ford'),
        (BMW, 'BMW'),
    ]

    name = models.CharField(max_length=255, blank=True)
    vehicle_number = models.CharField(max_length=255, unique=True)
    capacity = models.IntegerField()
    model = models.CharField(max_length=255, choices=VEHICLE_MODEL_CHOICES, blank=True)
    type = models.CharField(max_length=255, choices=VEHICLE_TYPE_CHOICES,  blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type} -> {self.model} -> {self.name}"
