from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13, blank=False)
    address = models.TextField()
    # user_type = models.TextChoices("USER", "")