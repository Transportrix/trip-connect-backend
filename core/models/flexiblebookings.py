from django.db import models
from django.contrib.auth import get_user_model
from core.models.users import User
from core.models.vehicles import Vehicle


class FlexibleBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    purpose = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)  # New field for payment status
    cost= models.DecimalField(max_digits=10, decimal_places=2)  # New field for rental price


    def __str__(self):
        return f"{self.user.username} booked {self.vehicle.name} from {self.start_date} to {self.end_date}"
