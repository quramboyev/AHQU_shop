from django.shortcuts import redirect, get_object_or_404, render
from cart.models import CartModel
from .models import OrderModel, OrderItemModel
from django.contrib.auth.decorators import login_required

@login_required
def order_create(request):
    cart = CartModel.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect('cart:cart_detail')
    order = OrderModel.objects.create(
        user=request.user,
        total_amount=cart.total_price(),
        full_name=f"{request.user.first_name} {request.user.last_name}",
        phone=request.user.phone_number,
        address="Адрес пользователя"  # Потом заменим на форму
    )
    for item in cart.items.all():
        OrderItemModel.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )
    cart.items.all().delete()  # очищаем корзину
    return redirect('order:order_detail', order.id)

@login_required
def order_detail(request, order_id):
    order = OrderModel.objects.get(id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})
