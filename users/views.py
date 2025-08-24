from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import CustomUserModel
from catalog.models import CategoryModel, ProductModel, ColorModel, ProductImageModel
from django.contrib.auth import get_user_model
import random

User = get_user_model()

def user_list_view(request):
    users = User.objects.all()
    products = ProductModel.objects.all()
    return render(request, 'home.html', {
        'users': users,
        'products': products})
