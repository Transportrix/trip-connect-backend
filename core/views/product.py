# your_app/views.py

from django.http import JsonResponse

from core.models.products import Product

def product_list(request):
    products = Product.objects.all().values('id', 'name', 'description', 'price', 'created_at')
    product_list = list(products)
    return JsonResponse(product_list, safe=False)
