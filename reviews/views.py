from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from .models import Review
from .serializers import (
    ReviewCreateSerializer,
    ReviewListSerializer
)
from products.models import Product


class ReviewListView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        reviews = product.reviews.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ReviewCreateSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"detail": "Review added"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, review_id):
        review = get_object_or_404(
            Review,
            id=review_id,
            user=request.user
        )
        review.delete()
        return Response(
            {"detail": "Review deleted"},
            status=status.HTTP_204_NO_CONTENT
        )
