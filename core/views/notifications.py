from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from core.models.notifications import Notification
from core.serializers.notification import NotificationSerializer


class NotificationListView(APIView):

    @swagger_auto_schema(
        operation_description="Create a new notification",
        request_body=NotificationSerializer,
        responses={201: NotificationSerializer, 400: "Bad Request"},
    )
    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NotificationDetailView(APIView):

    @swagger_auto_schema(
        operation_id="Notification Detail",
        operation_description="Retrieve notifications for a user",
        responses={200: NotificationSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                "user_id",
                openapi.IN_PATH,
                description="User ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def get(self, request, notification_id, user_id):
        notifications = Notification.objects.get(pk=notification_id)
        serializer = NotificationSerializer(notifications)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Delete a notification",
        responses={204: "No Content", 404: "Not Found"},
        manual_parameters=[
            openapi.Parameter(
                "user_id",
                openapi.IN_PATH,
                description="Notification ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def delete(self, request, notification_id, user_id):
        try:
            notification = Notification.objects.get(pk=notification_id, user=user_id)
            notification.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Notification.DoesNotExist:
            return Response(
                {"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND
            )


class GetNotificationByUserView(APIView):

    @swagger_auto_schema(
        operation_description="Retrieve notifications for a user",
        responses={200: NotificationSerializer(many=True)},
        manual_parameters=[
            openapi.Parameter(
                "user_id",
                openapi.IN_PATH,
                description="User ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def get(self, request, user_id):
        notifications = Notification.objects.filter(user_id=user_id).order_by(
            "-created_at"
        )
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MarkAsReadView(APIView):

    @swagger_auto_schema(
        operation_description="Mark a notification as read",
        responses={200: "Notification marked as read", 404: "Not Found"},   
        manual_parameters=[
            openapi.Parameter(
                "user_id",
                openapi.IN_PATH,
                description="Notification ID",
                type=openapi.TYPE_INTEGER,
            )
        ],
    )
    def post(self, request, notification_id, user_id):
        try:
            notification = Notification.objects.get(pk=notification_id, user=user_id)
            notification.is_read = True
            notification.save()
            return Response(
                {"message": "Notification marked as read"}, status=status.HTTP_200_OK
            )
        except Notification.DoesNotExist:
            return Response(
                {"error": "Notification not found"}, status=status.HTTP_404_NOT_FOUND
            )
