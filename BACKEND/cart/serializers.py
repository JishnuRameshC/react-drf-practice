from rest_framework import serializers
from .models import Cart, CartItem
from store.models import Product
from accounts.models import User

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'