from django.contrib import admin
from .models import CategoryModel, ColorModel, ProductModel, ProductImageModel
from parler.admin import TranslatableAdmin

admin.site.register(CategoryModel)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['name']

admin.site.register(ColorModel)
class ColorModelAdmin(TranslatableAdmin):
    list_display = ['name']

admin.site.register(ProductModel)
class ProductModelAdmin(TranslatableAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name')

admin.site.register(ProductImageModel)