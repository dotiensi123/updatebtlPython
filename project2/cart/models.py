from django.db import models
from book.models import Book
from django.contrib.auth.models import User
# Create your models here.
class Cart(models.Model):
    user =models.ForeignKey(User, on_delete= models.CASCADE)

class CartItem(models.Model):
    book = models.OneToOneField(Book, on_delete= models.CASCADE)    
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE)
    quantity = models.IntegerField(default=1)
