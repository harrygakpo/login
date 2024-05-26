from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.signin, name='signin' ),
    path('store1', views.product_list, name='product_list'),
    path('store', views.store, name='store'),
    path('checkout', views.checkout, name='checkout'),
]
