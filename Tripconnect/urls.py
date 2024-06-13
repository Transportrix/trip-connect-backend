
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from core.views.home import home


# from core import views
schema_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version="v1",
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [

    re_path(
    r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),


    path('', home),
    path('admin/', admin.site.urls),    
    path('api/products/',include('core.urls.product')),
    path('api/users/',include('core.urls.users')),
    path('api/drivers/',include('core.urls.drivers')),
    path('api/notifications/',include('core.urls.notifications')),
    path('api/reviews/',include('core.urls.reviews')),
    path('api/vehicles/',include('core.urls.vehicles')),
    path('api/bookings/',include('core.urls.bookings')),



    # path("", views.index, name="index"),
    # path("bookings/", include('core.urls.bookings')),
    # path("users", views.index, name="index"),
    # path("reviews", views.index, name="index"),



]
