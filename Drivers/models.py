from django.db import models

# Create your models here.
class Drivers(models.Model):
    name = models.TextField(max_length=255)
    contact = models.TextField(max_length=13)
    email = models.EmailField(blank=True)