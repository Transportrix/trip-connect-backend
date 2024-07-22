from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    uid = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)

    # Add other common user attributes as needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username