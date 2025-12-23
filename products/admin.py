from django.contrib import admin

from .models import Product, Category, Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('title',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    search_fields = ('title',)