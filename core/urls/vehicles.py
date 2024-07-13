from django.urls import path
from core.views.vehicles import VehicleList, VehicleDetail, VehicleWithSchedules, SearchVehicleWithSchedule

urlpatterns = [
    path('', VehicleList.as_view(), name='vehicle-list'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),
    path('vehicles-with-schedules/', VehicleWithSchedules.as_view(), name='vehicle-with-schedules'),
    path('search-vehicle-with-schedule/', SearchVehicleWithSchedule.as_view(), name='search-vehicle-with-schedule'),
]
