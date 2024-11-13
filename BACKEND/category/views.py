from rest_framework import viewsets
from .serializers import CategorySerializer, SubcategorySerializer
from .models import Category, Subcategory


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

