from django.contrib import admin

from .models import Product, Category, Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass