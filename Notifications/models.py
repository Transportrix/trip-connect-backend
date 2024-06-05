from django.db import models
from Users.models import Users


# Create your models here.
class Notifications(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.TextField(max_length=255)
    message = models.TextField(max_length=255)
    # status = models.TextChoices(
    #     "promotion",
    #     "reminder",
    #     "rating reminder"
    # )
    timestamp = models.DateField(auto_created=True)
