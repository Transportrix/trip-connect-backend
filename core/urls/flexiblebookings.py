# urls.py
from django.urls import path

from core.views.flexiblebookings import (
    FLBSetPaymentStatusView,
    FlexibleBookingDetailView,
    FlexibleBookingListView,
    FlexibleBookingListViewByUser,
)

urlpatterns = [
    path(
        "",
        FlexibleBookingListView.as_view(),
        name="flexiblebooking-list-create",
    ),
    path(
        "<int:pk>/", FlexibleBookingDetailView.as_view(), name="flexiblebooking-detail"
    ),
    path(
        "users/<int:pk>/",
        FlexibleBookingListViewByUser.as_view(),
        name="flexiblebooking-list-create",
    ),
    path(
        "<int:booking_id>/set-paid/",
        FLBSetPaymentStatusView.as_view(),
        name="set-payment-status",
    ),
    # other paths
]
