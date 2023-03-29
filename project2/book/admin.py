from django.contrib import admin
from .models import Book, Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id','name')
    search_fields = ['name']
    list_filter = ('category_id','name')
admin.site.register(Book)
admin.site.register(Category)