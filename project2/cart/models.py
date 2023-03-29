from django.db import models
from book.models import Book
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_cart_total(self):
        total = 0
        for item in self.cartitem_set.all():
            total += item.get_item_price()
        return total

class CartItem(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_item_price(self):
        return self.book.price * self.quantity
