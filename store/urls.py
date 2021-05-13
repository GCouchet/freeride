from store.models import Order
from django.db.models import base
from django.shortcuts import render_to_response
from rest_framework import routers
from .views import CustomerViewSet, ProductViewSet, OrderViewSet, OrderItemViewSet, ShippingAddressViewSet


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet, basename='customer')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'order', OrderViewSet, basename='order')
router.register(r'order_item', OrderItemViewSet, basename='order_item')
router.register(r'shipping_address', ShippingAddressViewSet, basename='shipping_address')

urlpatterns = router.urls
