from django.urls import path
from .views import (
    ReviewListView,
    ReviewCreateView,
    ReviewDeleteView
)

urlpatterns = [
    path('product/<int:product_id>/', ReviewListView.as_view()),
    path('create/', ReviewCreateView.as_view()),
    path('delete/<int:review_id>/', ReviewDeleteView.as_view()),
]
