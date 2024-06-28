from django.urls import path

from core.views.drivers import Driver, Driverlist

urlpatterns = [
    path('', Driver.as_view(), name='driver_list'),
    path('<int:pk>/', Driver.as_view(),  name='driver_detail'),
]
