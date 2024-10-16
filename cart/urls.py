from django.urls import path
from .views import CartView, CartDetailView, CartQuantityIncrease, CartQuantityDecrease, CheckOut

urlpatterns = [
    path('view/', CartView.as_view(), name='view'),
    path('detail/<int:pk>',CartDetailView.as_view(), name='detail'),
    path('increase/<int:pk>',CartQuantityIncrease.as_view(), name='increase'),
    path('decrease/<int:pk>',CartQuantityDecrease.as_view(), name='decrease'),
    path('checkout/',CheckOut.as_view(), name='checkout'),
]
