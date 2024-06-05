from django.contrib import admin
from django.urls import include, path

from core.views.product import product_list

# from core import views

urlpatterns = [
    path("", product_list, name="product_list"),
]
