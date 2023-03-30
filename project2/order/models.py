from django.db import models
from cart.models import Cart
from django.contrib.auth.models import User

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('0', 'uncompleted'),
        ('1', 'completed'),
    ]
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default='0')
    order_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.order_id}, {self.cart.cart_id}, {self.user.username}"