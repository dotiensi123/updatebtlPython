from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, Cart
from cart.models import CartItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

@login_required(login_url='User:login')
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            user = request.user
            cart_items = CartItem.objects.filter(cart__user=user)
            if cart_items.exists():
                cart = cart_items[0].cart
            else:
                cart = Cart.objects.create(user=user)
            order = form.save(commit=False)
            order.cart = cart
            order.user = user
            order.save()
            for item in cart_items:
                item.delete()
            return redirect('orders:order_detail', order_id=order.order_id)
    else:
        form = OrderForm()
    return render(request, 'create_order.html', {'form': form})

@login_required(login_url='User:login')
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_id')
    return render(request, 'order_list.html', {'orders': orders})



# def order_detail(request, order_id):
#     order = get_object_or_404(Order, order_id=order_id)
#     cart_items = CartItem.objects.filter(cart=order.cart)
#     context = {
#         'order': order,
#         'cart_items': cart_items
#     }
#     if request.method == 'POST':
#         order.status = request.POST.get('status')
#         order.save()
#     return render(request, 'order_detail.html', context)

@login_required(login_url='User:login')
def order_detail(request, order_id):
    order = get_object_or_404(Order, order_id=order_id)
    cart_items = CartItem.objects.filter(cart=order.cart)
    context = {
        'order': order,
        'cart_items': cart_items,
    }
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
    return render(request, 'order_detail.html', context)
