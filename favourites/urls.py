from django.urls import path
from .views import (
    FavoriteListView,
    FavoriteAddView,
    FavoriteRemoveView
)

urlpatterns = [
    path('', FavoriteListView.as_view()),
    path('add/', FavoriteAddView.as_view()),
    path('remove/<int:product_id>/', FavoriteRemoveView.as_view()),
]
