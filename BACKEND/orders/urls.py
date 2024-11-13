from django.urls import path
from .views import OrderView, OrderRetrieveUpdateDestroyView, OrderProductView, OrderProductRetrieveUpdateDestroyView, PaymentView, PaymentRetrieveUpdateDestroyView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order-list-create'),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyView.as_view(), name='order-detail'),
    path('orderproduct/', OrderProductView.as_view(), name='orderproduct-list-create'),
    path('orderproduct/<int:pk>/', OrderProductRetrieveUpdateDestroyView.as_view(), name='orderproduct-detail'),
    path('payment/', PaymentView.as_view(), name='payment-list-create'),
    path('payment/<int:pk>/', PaymentRetrieveUpdateDestroyView.as_view(), name='payment-detail'),
]
