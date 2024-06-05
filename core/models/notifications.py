from django.db import models

from core.models.users import User


# Create your models here.
class Notification(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    message = models.TextField(max_length=255)
    # status = models.TextChoices(
    #     "promotion",
    #     "reminder",
    #     "rating reminder"
    # )
    timestamp = models.DateField(auto_created=True)
