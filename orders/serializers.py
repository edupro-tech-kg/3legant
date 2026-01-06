from rest_framework import serializers
from .models import Order, OrderItem
from cart.models import Cart, CartItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'total_price', 'created_at', 'updated_at', 'items']

    def create(self, validated_data):
        user = self.context['request'].user

        try:
            cart = Cart.objects.get(user=user)
        except Cart.DoesNotExist:
            raise serializers.ValidationError("У пользователя нет корзины.")

        cart_items = CartItem.objects.filter(cart=cart)
        if not cart_items.exists():
            raise serializers.ValidationError("Корзина пуста.")

        order = Order.objects.create(user=user, total_price=0)
        total = 0

        for item in cart_items:
            price = item.product.price * item.quantity
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=price
            )
            total += price

        order.total_price = total
        order.save()

        cart_items.delete()
        return order
