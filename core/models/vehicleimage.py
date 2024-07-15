from django.db import models
from cloudinary.models import CloudinaryField

from core.models.vehicles import Vehicle

class VehicleImage(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='images', on_delete=models.CASCADE)
    image = CloudinaryField('image',  folder='tripconnect')

    def __str__(self):
        return f"Image {self.id} for {self.vehicle.vehicle_number}"
