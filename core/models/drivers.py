from django.db import models
from core.models.users import User


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='driver_profile')
    license_number = models.CharField(max_length=255, unique=True)
    driving_experience = models.IntegerField(default=0)  # Example driver-specific attribute
    # Add other driver-specific attributes as needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
