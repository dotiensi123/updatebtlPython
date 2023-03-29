from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('category/',views.get_category,name = 'category'),
    path('category/book/<int:id>/',views.get_book,name = 'bookOfCategory'),
    path('category/create/', views.create_category, name='category_create'),
    # # path('category/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:id>/', views.delete_category, name='category_delete'),
    
    path('', views.book_list, name='book_list'),
    path('book/create/', views.book_create, name='book_create'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>', views.book_edit, name='book_edit'),
    path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('search/', views.book_search, name='book_search'),
    # path('bookview/<int:pk>',views.view_document,name = 'view_document'),
]

    

