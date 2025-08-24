from django.urls import path
from .views import list_products, product_detail,create_product
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns=[
    path("products/", list_products, name="list_products"),
    path("products/<int:id>/",product_detail,name="product_detail"),
    path('', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('products/create/',create_product, name="create_product"),
]
