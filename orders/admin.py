from django.contrib import admin
from .models import OrderItemModel, OrderModel

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 0

@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'phone', 'status', 'total_price', 'created_at']
    inlines = [OrderItemInline]

admin.site.register(OrderItemModel)