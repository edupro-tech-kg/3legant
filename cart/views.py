from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import  Product
from .serializers import CartItemSerializer
from rest_framework.response import Response
from .models import Cart, CartItem





class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = cart.items.all()

        serializer = CartItemSerializer(items, many=True)
        total = sum(
            item.product.price * item.quantity
            for item in items
        )

        return Response({
            "items": serializer.data,
            "total": total
        })



class AddToCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        product_id = request.data.get("product_id")
        quantity = int(request.data.get("quantity", 1))

        if quantity < 1:
            return Response(
                {"error": "Quantity must be >= 1"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Product not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        cart, _ = Cart.objects.get_or_create(user=request.user)

        item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product
        )

        if created:
            item.quantity = quantity
        else:
            item.quantity += quantity

        item.save()

        return Response({"message": "Added to cart"})


class RemoveFromCartAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        item = CartItem.objects.filter(
            id=item_id,
            cart__user=request.user
        ).first()

        if not item:
            return Response(
                {"error": "Item not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        item.delete()
        return Response(
            {"message": "Removed"},
            status=status.HTTP_204_NO_CONTENT
        )
