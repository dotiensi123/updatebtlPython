from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name},{self.category_id}"

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    file = models.FileField()
    image = models.ImageField()
    
    def __str__(self):
        return f"{self.book_id},{self.category_id},{self.name},{self.price},{self.description}"
