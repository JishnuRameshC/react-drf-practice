from django.shortcuts import render
from rest_framework import generics
from .serializers import CartSerializer, CartItemSerializer
from .models import Cart, CartItem
# Create your views here.

class CartView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class CartRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class CartItemView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

class CartItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()
