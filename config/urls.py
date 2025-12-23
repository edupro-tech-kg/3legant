from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from articles.views import ArticleListAPIView  # путь к твоему view

# создаём router
router = routers.SimpleRouter()
router.register(r'article', ArticleListAPIView, basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/token/refresh/', TokenRefreshView.as_view()),
    path('api/auth/', include('accounts.urls')),

    path('api/', include('products.urls')),
    path('api/', include('search.urls')),
    path('api/newsletter/', include('newsletter.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/favorites/', include('favourites.urls')),
    path('api/reviews/', include('reviews.urls')),

    path('api/articles/', include('articles.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
