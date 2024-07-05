from django.urls import path

from core.views.drivers import DriverDetail, Driverlist

urlpatterns = [
    path('', Driverlist.as_view(), name='driver_list_create'),
    path('<int:pk>/', DriverDetail.as_view(),  name='driver_detail'),
]

