# urls.py
from django.urls import path

from core.views.flexiblebookings import FlexibleBookingDetailView, FlexibleBookingListView

urlpatterns = [
    path('', FlexibleBookingListView.as_view(), name='flexiblebooking-list-create'),
    path('<int:pk>/', FlexibleBookingDetailView.as_view(), name='flexiblebooking-detail'),
    # other paths
]
