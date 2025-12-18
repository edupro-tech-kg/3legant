from rest_framework import serializers
from .models import Favorite


class FavoriteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('product',)

    def validate(self, data):
        user = self.context['request'].user
        if Favorite.objects.filter(
            user=user,
            product=data['product']
        ).exists():
            raise serializers.ValidationError(
                "Product already in favorites"
            )
        return data

from products.serializers import ProductSerializer


class FavoriteListSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ('id', 'product', 'created_at')
