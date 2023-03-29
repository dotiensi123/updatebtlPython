from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Cart, CartItem
from book.models import Book

@login_required
def add_to_cart(request, book_id):
    book = Book.objects.get(pk=book_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, cart_item_created = CartItem.objects.get_or_create(book=book, cart=user_cart)

    if not cart_item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()
    cart_items = cart.cartitem_set.all() if cart else []
    total_price = 0
    for item in cart_items:
        total_price += item.get_item_price()
    return render(request, 'cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
@require_POST
def update_quantity(request, item_id):
    quantity = request.POST.get('quantity')
    item = get_object_or_404(CartItem, id=item_id)
    if quantity and quantity.isdigit() and int(quantity) > 0 and int(quantity) <= 10:
        item.quantity = int(quantity)
        item.save()
    return redirect('cart:cart_detail')

@login_required
@require_POST
def remove_from_cart(request, item_pk):
    item = get_object_or_404(CartItem, pk=item_pk)
    item.delete()
    return redirect('cart:cart_detail')
