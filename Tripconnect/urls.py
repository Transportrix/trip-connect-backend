
from django.contrib import admin
from django.urls import include, path

# from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", views.index, name="index"),
    # path("bookings/", include('core.urls.bookings')),
    # path("users", views.index, name="index"),
    # path("reviews", views.index, name="index"),



]
