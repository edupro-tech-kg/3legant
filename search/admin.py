from django.contrib import admin
from .models import SearchQueryLog

@admin.register(SearchQueryLog)
class SearchQueryLogAdmin(admin.ModelAdmin):
    list_display = ( "query", "results_count", "created_at")
    search_fields = ("query",)
    readonly_fields = ("query", "results_count", "created_at")

'''
from apps.products.models import Product


@admin.register(Product)
class ProductSearchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "brand",
        "category",
        "price",
        "in_stock",
    )
    search_fields = (
        "name",
        "brand",
        "category",
    )
    list_filter = (
        "brand",
        "category",
        "in_stock",
    )

'''