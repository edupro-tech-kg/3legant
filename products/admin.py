from django.contrib import admin

from .models import Product, Category, Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'brand', 'in_stock', 'is_popular', 'created_at')
    list_filter = ('category', 'brand', 'in_stock', 'is_popular', 'created_at')
    search_fields = ('title', 'description')
    autocomplete_fields = ('category', 'brand')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)