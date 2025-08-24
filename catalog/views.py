from django.shortcuts import render, redirect
from .models import CategoryModel, ProductModel, ColorModel, ProductImageModel

def category_list_view(request):
    categories = CategoryModel.objects.filter(parent__isnull=True)
    return render(request, 'catalog/category_list.html', {'categories': categories})

def product_list_view(request, category_id=None):
    products = ProductModel.objects.all()
    return render(request, 'home.html', {'products': products}) 
