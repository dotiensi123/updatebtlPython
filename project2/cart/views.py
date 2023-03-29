from book.models import Book
from cart.models import Cart, CartItem
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import UpdateQuantityForm
from django.contrib.auth import decorators
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

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
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = user_cart.cartitem_set.all()

    total_price = sum([item.book.price * item.quantity for item in cart_items])

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart_detail.html', context)

@require_POST
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    quantity = int(request.POST['quantity'])
    if quantity > 0:
        item.quantity = quantity
        item.save()
    else:
        item.delete()
    return redirect('cart:cart_detail')

@login_required
@require_POST
def remove_from_cart(request, item_pk):
    item = get_object_or_404(CartItem, pk=item_pk)
    item.delete()
    return redirect('cart:cart_detail')
