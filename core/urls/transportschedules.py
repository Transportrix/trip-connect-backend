from django.urls import path

from core.views.transportschedules import (
    TransportSchedulesDetail,
    TransportSchedulesList,
    TransportTravellingFromToList,
)

urlpatterns = [
    path("", TransportSchedulesList.as_view(), name="transport-schedules-list"),
    path(
        "from-to/",
        TransportTravellingFromToList.as_view(),
        name="transport-from-to-list",
    ),
    path(
        "<int:pk>/",
        TransportSchedulesDetail.as_view(),
        name="transport-schedules-detail",
    ),
]
