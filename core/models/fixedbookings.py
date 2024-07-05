from django.db import models

from core.models.busschedules import BusSchedule
from core.models.users import User


class FixedBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_schedule = models.ForeignKey(BusSchedule, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, default='booked')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)