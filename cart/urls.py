from django.urls import path
from .views import CartView, AddToCart

urlpatterns = [
    path('', CartView.as_view()),        # GET /api/cart/ → список товаров + сумма
    path('add/', AddToCart.as_view()),   # POST /api/cart/add/ → добавить товар
]
