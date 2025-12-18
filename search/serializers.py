from rest_framework import serializers
from products.models import Product


class SearchProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "brand",
            "category",
            "price",
            "in_stock",
        )

class SuggestSerializer(serializers.Serializer):
    value = serializers.CharField()

