from django.urls import path, include
from .views import (
    CartView,
    AddToCartAPIView,
    RemoveFromCartAPIView,
    OrderViewSet
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet, basename='orders')

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("add/", AddToCartAPIView.as_view(), name="add-to-cart"),
    path("remove/<int:item_id>/", RemoveFromCartAPIView.as_view(), name="remove-from-cart"),
    path('api/', include(router.urls)),
]
