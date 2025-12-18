from django.urls import path
from .views import ProductSearchView, ProductSuggestView

# Django ожидает переменную с именем `urlpatterns`
urlpatterns = [
    path('search/', ProductSearchView.as_view()),
    path('suggest/', ProductSuggestView.as_view()),
]