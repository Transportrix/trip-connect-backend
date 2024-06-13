from django.urls import path

from core.views.product import ProductDetail, ProductList

urlpatterns = [
    path('', ProductList.as_view(), name='product_list_create'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
]
