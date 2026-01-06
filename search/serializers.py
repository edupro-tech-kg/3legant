from rest_framework import serializers
from products.models import Product


class SearchProductSerializer(serializers.ModelSerializer):
    brand = serializers.CharField(source="brand.title", read_only=True)
    category = serializers.CharField(source="category.title", read_only=True)
    
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "brand",
            "category",
            "price",
            "in_stock",
        )


class SuggestSerializer(serializers.Serializer):
    value = serializers.CharField()

