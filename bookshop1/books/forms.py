from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'description', 'price', 'image_url', 'stock']
        
        
class SearchForm(forms.Form):
    search_term = forms.CharField(label='Tìm kiếm', max_length=100)