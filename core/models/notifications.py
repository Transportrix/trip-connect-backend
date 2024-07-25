from django.db import models
from core.models.users import User

class Notification(models.Model):
    ALERT = 'alert'
    REMINDER = 'reminder'
    UPDATE = 'update'
    MESSAGE = 'message'

    TYPE_CHOICES = [
        (ALERT, 'Alert'),
        (REMINDER, 'Reminder'),
        (UPDATE, 'Update'),
        (MESSAGE, 'Message'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    read = models.BooleanField(default=False)
    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        default=ALERT,
    )
    status = models.CharField(max_length=255, default='unread')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
