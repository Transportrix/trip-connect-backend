from django.urls import path

from core.views.drivers import DriverDetail, DriverList

urlpatterns = [
    path('', DriverList.as_view(), name='driver_list'),
    path('<int:pk>/', DriverDetail.as_view(),  name='driver_detail'),
]
