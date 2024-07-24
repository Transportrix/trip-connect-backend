from django.db import models

from core.models.transportschedules import TransportBusesAndSchedules, TransportSchedules
from core.models.users import User


class FixedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_and_schedule = models.ForeignKey(TransportBusesAndSchedules, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(default=False)  # New field for payment status
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # New field for rental price
    


    def __str__(self):
        return f"No. {self.id} - by: {self.user.username}, Bus Schedule: {self.bus_and_schedule}"