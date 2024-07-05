from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)

    # is_driver = models.BooleanField(default=False)  # Indicates if the user is a driver
    # Add other common user attributes as needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username