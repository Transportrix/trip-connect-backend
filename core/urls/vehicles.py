from django.urls import path
from core.views.vehicles import VehicleList, VehicleDetail, VehicleWithSchedules, SearchVehicleWithSchedule

urlpatterns = [
    path('', VehicleList.as_view(), name='vehicle-list'),
    path('<int:pk>/', VehicleDetail.as_view(), name='vehicle-detail'),

]
