from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404

from .models import Favorite
from .serializers import (
    FavoriteCreateSerializer,
    FavoriteListSerializer
)
from products.models import Product


class FavoriteListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteListSerializer(favorites, many=True)
        return Response(serializer.data)


class FavoriteAddView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = FavoriteCreateSerializer(
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"detail": "Added to favorites"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FavoriteRemoveView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, product_id):
        favorite = get_object_or_404(
            Favorite,
            user=request.user,
            product_id=product_id
        )
        favorite.delete()
        return Response(
            {"detail": "Removed from favorites"},
            status=status.HTTP_204_NO_CONTENT
        )
