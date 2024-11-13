from .views import CartItemView, CartItemRetrieveUpdateDestroyView, CartView, CartRetrieveUpdateDestroyView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('cart', CartView)
router.register('cartitem', CartItemView)   

urlpatterns = [
    path('cartitem/', CartItemView.as_view()),  
    path('cart/', CartView.as_view()),
    path('cartitem/<int:pk>/', CartItemRetrieveUpdateDestroyView.as_view()),
    path('cart/<int:pk>/', CartRetrieveUpdateDestroyView.as_view()),
]
