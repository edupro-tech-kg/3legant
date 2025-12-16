from django.urls import path
from .views import ProductSearchView, ProductSuggestView

url_patterns = [
    path('search/', ProductSearchView.as_view(), name = 'search'),
    path('suggest/', ProductSuggestView.as_view(), name = 'suggest')
]