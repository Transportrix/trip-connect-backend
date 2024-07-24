from django.urls import path

from core.views.fixedbookings import BookingsDetail, BookingsList, SetPaymentStatusView

urlpatterns = [
    path('users/<int:user_id>/', BookingsList.as_view(), name='_list'),
    path('<int:booking_id>/users/<int:user_id>/', BookingsDetail.as_view(), name='_detail'),
    path('<int:booking_id>/set-paid/', SetPaymentStatusView.as_view(), name='set-payment-status'),

]
