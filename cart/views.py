from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import ProductModel
from .models import CartModel, CartItemModel

@login_required
def cart_detail(request):
    cart, _ = CartModel.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(ProductModel, id=product_id)
    cart, _ = CartModel.objects.get_or_create(user=request.user)
    item, created = CartItemModel.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('cart:cart_detail')

@login_required
def cart_remove(request, item_id):
    item = get_object_or_404(CartItemModel, id=item_id, cart__user=request.user)
    item.delete()
    return redirect('cart:cart_detail')