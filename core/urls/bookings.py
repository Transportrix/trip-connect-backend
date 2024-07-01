from django.urls import path

from core.views.bookings import BookingsDetail, BookingsList
from core.views.product import ProductDetail, ProductList

urlpatterns = [
    path('', BookingsList.as_view(), name='_list'),
    path('<int:pk>/', BookingsDetail.as_view(), name='_detail'),
]
