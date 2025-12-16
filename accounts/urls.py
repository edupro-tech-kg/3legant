from django.urls import path
from .views import RegisterView, PasswordResetView, LogoutView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('password-reset/', PasswordResetView.as_view()),
    path('logout/', LogoutView.as_view()),
]
