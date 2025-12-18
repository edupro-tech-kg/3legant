from django.urls import path
from .views import ProductSearchView, ProductSuggestView

url_patterns = [
    path('search/', ProductSearchView.as_view()),
    path('suggest/', ProductSuggestView.as_view())
]