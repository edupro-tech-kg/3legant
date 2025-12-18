from django.urls import path
from .views import (
    SubscribeView,
    UnsubscribeView,
    SendNewsletterView
)

urlpatterns = [
    path('subscribe/', SubscribeView.as_view()),
    path('unsubscribe/', UnsubscribeView.as_view()),
    path('send/', SendNewsletterView.as_view()),
]
