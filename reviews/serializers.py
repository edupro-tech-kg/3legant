from rest_framework import serializers
from .models import Review


class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('product', 'rating', 'comment', 'image')

    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError(
                "Rating must be between 1 and 5"
            )
        return value

    def validate(self, data):
        user = self.context['request'].user
        product = data['product']

        if Review.objects.filter(user=user, product=product).exists():
            raise serializers.ValidationError(
                "You already reviewed this product"
            )
        return data

class ReviewListSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = (
            'id',
            'user',
            'rating',
            'comment',
            'image',
            'created_at'
        )
