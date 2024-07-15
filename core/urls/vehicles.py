from django.urls import path

from core.views.vehicles import VehicleModelListView, VehicleSearchView, VehicleTypeListView

urlpatterns = [
    path('models/', VehicleModelListView.as_view(), name='vehicle-models'),
    path('types/', VehicleTypeListView.as_view(), name='vehicle-types'),
    path('', VehicleSearchView.as_view(), name='search-vehicles'),
]
