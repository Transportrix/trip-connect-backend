from django.db import models

from core.models.fixedbookings import FixedBooking


class BookedSeat(models.Model):
    booking = models.ForeignKey(
        FixedBooking, related_name="booked_bus_seats", on_delete=models.CASCADE
    )
    seat_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
