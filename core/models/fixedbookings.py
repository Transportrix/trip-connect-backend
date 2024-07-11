from django.db import models

from core.models.transportschedules import TransportSchedules
from core.models.users import User


class FixedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_schedule = models.ForeignKey(TransportSchedules, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"No. {self.id} - by: {self.user.username}, Bus Schedule: {self.bus_schedule}"