from django.shortcuts import render,get_object_or_404

from .import models

def product_detail(request, id, slug):
    product = models.Product.objects.get(id=id,slug=slug)
    return render(request,'product/detail.html', {'product' : product})

def category(request):
    category = models.Category.objects.all()
    return render(request, 'product/category.html', {'categorys' : category })

# Create your views here.

