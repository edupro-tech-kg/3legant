from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, CartItem, Product

class CartView(APIView):
    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = []
        total = 0
        for item in cart.items.all():
            items.append({
                "product": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity,
                "sum": item.product.price * item.quantity
            })
            total += item.product.price * item.quantity
        return Response({"items": items, "total": total})

class AddToCart(APIView):
    def post(self, request):
        product_id = request.data['product_id']
        qty = request.data.get('quantity', 1)

        cart, _ = Cart.objects.get_or_create(user=request.user)
        product = Product.objects.get(id=product_id)

        item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            item.quantity += qty
        item.save()

        return Response({"ok": True})
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Cart, CartItem

class CartView(APIView):
    permission_classes = [IsAuthenticated]  # 🔹 защита от AnonymousUser

    def get(self, request):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        items = []
        total = 0
        for item in cart.items.all():
            items.append({
                "product": item.product.name,
                "price": item.product.price,
                "quantity": item.quantity,
                "sum": item.product.price * item.quantity
            })
            total += item.product.price * item.quantity
        return Response({"items": items, "total": total})
