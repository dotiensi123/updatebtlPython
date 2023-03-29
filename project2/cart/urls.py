from django.urls import path
from .import views
app_name = 'cart'

urlpatterns = [
    path('add/<int:book_id>/',views.add_to_cart , name='add_to_cart'),
    path('view/', views.cart_detail, name='cart_detail'),
    path('update_quantity/<int:item_id>/', views.update_quantity, name='update_quantity'),
    path('remove_from_cart/<int:item_pk>/', views.remove_from_cart, name='remove_from_cart'),
]
