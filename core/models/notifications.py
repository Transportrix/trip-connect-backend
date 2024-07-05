from django.db import models

from core.models.users import User
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=255, default='unread')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)