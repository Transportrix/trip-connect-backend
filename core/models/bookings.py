from django.db import models

from core.models.users import User
from core.models.vehicles import Vehicle


# Create your models here.
class Booking(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # booking_status = models.TextChoices("pending","approved","declined")
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    pickup_time = models.DateTimeField()
    distance = models.IntegerField()
    # distance_unit = models.TextChoices("KM","M","Miles")
    fare = models.IntegerField()
    destination = models.TextField(max_length=255)
