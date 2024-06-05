from django.db import models
from Bookings.models import Bookings
from Users.models import Users
from Drivers.models import Drivers

# Create your models here.
class Reviews(models.Model):
    booking_id = models.ForeignKey(Bookings, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    driver_id = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    rating = models.IntegerField() # Add validation for (1 - 5)
    review = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_created=True)