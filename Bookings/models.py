from django.db import models
from  Users.models import Users
from Vehicles.models import Vehicles

# Create your models here.
class Bookings(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    # booking_status = models.TextChoices("pending","approved","declined")
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField()
    distance = models.IntegerField()
    # distance_unit = models.TextChoices("KM","M","Miles")
    fare = models.IntegerField()
    destination = models.TextField(max_length=255)
