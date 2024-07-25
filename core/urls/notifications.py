from django.urls import path

from core.views.notifications import (
    MarkAsReadView,
    GetNotificationByUserView,
    NotificationDetailView,
    NotificationListView,
)


urlpatterns = [
    path(
        "",
        NotificationListView.as_view(),
        name="notification-list",
    ),
    path(
        "users/<int:user_id>/",
        GetNotificationByUserView.as_view(),
        name="notification-user",
    ),
    path(
        "<int:notification_id>/users/<int:user_id>/",
        NotificationDetailView.as_view(),
        name="notification-user-detail",
    ),
    path(
        "<int:notification_id>/users/<int:user_id>/mark-as-read/",
        MarkAsReadView.as_view(),
        name="notification-mark-as-read",
    ),
]
