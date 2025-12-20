from django.urls import path
from .views import (ProductListView, ProductDetailView,
                    CategoryListView, BrandListView,
                    ProductByCategoryView, ProductByBrandView,
                    NewProductView, PopularProductView)

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("products/<int:product_id>/", ProductDetailView.as_view()),
    path("categories/", CategoryListView.as_view()),
    path("brands/", BrandListView.as_view()),
    path("categories/<int:category_id>/products/", ProductByCategoryView.as_view()),
    path("brands/<int:brand_id>/products/", ProductByBrandView.as_view()),
    path("new/products/", NewProductView.as_view()),
    path("popular/products/", PopularProductView.as_view())
]