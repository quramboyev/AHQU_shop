from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from catalog.models import ProductModel

User = get_user_model()

class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В ожидании'),
        ('confirmed', 'Подтвержден'),
        ('shipped', 'Отправлен'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ #{self.id} - {self.full_name}"

    def calculate_total(self):
        total = sum(item.get_total_price() for item in self.items.all())
        self.total_price = total
        self.save()
        return total
    

class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Order item"
        verbose_name_plural = "Order items"

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def get_total_price(self):
        return self.quantity * self.price
    