from django.shortcuts import render
from product.models import Product


def home(request):
    product = Product.objects.all()
    return render(request, 'home.html', {'Prodycts': product} )

















