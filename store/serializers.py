from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem, ShippingAddress


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'user', 'email', 'phone']


class ProductSerializer(serializers.ModelSerializer):
    image_url_location = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['name', 'price', 'digital', 'description', 'image']

    def get_image_url_location(self, obj):
        return obj.image.url if obj.image else ""


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer', 'date_ordered', 'complete', 'transaction_id']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'order', 'address', 'quantity', 'date_added']


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['customer', 'order', 'address', 'date', 'time']