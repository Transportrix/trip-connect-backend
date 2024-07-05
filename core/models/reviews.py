# from django.db import models
# from core.models.bookings import Booking
# from core.models.drivers import Driver
# from core.models.users import User


# # Create your models here.
# class Review(models.Model):
#     booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
#     user_id = models.ForeignKey(User, on_delete=models.CASCADE)
#     driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
#     rating = models.IntegerField() # Add validation for (1 - 5)
#     review = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_created=True)