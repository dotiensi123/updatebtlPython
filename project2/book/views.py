from django.shortcuts import render,get_object_or_404,redirect
from .models import Book as bookModel
from .models import Category as categoryModel
from .forms import BookForm,CategoryForm
from django.http import HttpResponse
from django.contrib.auth import decorators
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required



def book_list(request):
    books = bookModel.objects.all()
    return render(request, 'book_list.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(bookModel, pk=pk)
    return render(request, 'book_detail.html', {'book': book})

@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect('book:book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'form.html', {'form': form})

@login_required
def book_edit(request, pk):
    book = get_object_or_404(bookModel, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect('book:book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'form.html', {'form': form})

@login_required
def book_delete(request, pk):
    book = get_object_or_404(bookModel, pk=pk)
    book.delete()
    return redirect('book:book_list')


# category views
 

def get_category(request):
    category_list = categoryModel.objects.filter().order_by('category_id')
    context = {'category_list': category_list}
    return render(request, 'category_list.html', context)

def get_book(request,id):
    books = bookModel.objects.filter(category_id = id)
    return render(request, 'book_list.html', {'books': books})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('book:category')
    else:
        form = CategoryForm()
        return render(request, 'form.html', {'form': form})
    
@login_required
def delete_category(request, id):
    category = get_object_or_404(categoryModel, category_id =id)
    category.delete()
    return redirect('book:category')

def book_search(request):
    query = request.GET.get('query')
    if query:
        books = bookModel.objects.filter(name__icontains=query) | bookModel.objects.filter(author__icontains=query) 
        context = {
            'books': books,
        }
        return render(request, 'book_list.html', context) # Trả về trang kết quả
    else:
        return render(request, 'book_list.html') # Trả về trang search nếu không có query

    