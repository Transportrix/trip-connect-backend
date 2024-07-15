from django.urls import path

from core.views.fixedbookings import BookingsDetail, BookingsList

urlpatterns = [
    path('users/<int:user_id>/', BookingsList.as_view(), name='_list'),
    path('<int:booking_id>/users/<int:user_id>/', BookingsDetail.as_view(), name='_detail'),
]
