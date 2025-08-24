from django.urls import path
from .views import category_list_view,product_list_view

app_name = 'catalog'

urlpatterns = [
    path('', category_list_view, name='category_list'),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:category_id>/', product_list_view, name='product_list_by_category'),
]
