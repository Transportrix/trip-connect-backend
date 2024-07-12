from django.urls import path

from core.views.bookings import BookingsDetail, BookingsList

urlpatterns = [
    path('', BookingsList.as_view(), name='_list'),
    path('<int:booking_id>/', BookingsDetail.as_view(), name='_detail'),
]
