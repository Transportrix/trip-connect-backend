from core.models.notifications import Notification
from rest_framework import serializers



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'