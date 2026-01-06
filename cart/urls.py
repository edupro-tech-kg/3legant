from django.urls import path
from .views import (
    CartView,
    AddToCartAPIView,
    RemoveFromCartAPIView,
)


urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add/", AddToCartAPIView.as_view(), name="add-to-cart"),
    path("remove/<int:item_id>/", RemoveFromCartAPIView.as_view(), name="remove-from-cart"),
]
