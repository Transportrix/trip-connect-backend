from django.urls import path
from core.views.transportbus import SearchTransportBusWithSchedule, TransportBusWithSchedules
from core.views.vehicles import VehicleList, VehicleDetail, VehicleWithSchedules, SearchVehicleWithSchedule

urlpatterns = [
    path('transport-buses-with-schedules/', TransportBusWithSchedules.as_view(), name='vehicle-with-schedules'),
    # path('search-transport-buses-with-schedule/', SearchTransportBusWithSchedule.as_view(), name='search-vehicle-with-schedule'),
]
