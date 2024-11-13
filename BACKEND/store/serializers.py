from rest_framework import serializers
from store.models import Product, ProductGallery


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    discount_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand_name', 'category', 'subcategory', 'description', 
                 'price', 'discount_percentage', 'discount_price', 'stock', 
                 'is_available', 'average_rating', 'product_image']
        read_only_fields = ['slug']
    
    def get_average_rating(self, obj):
        return obj.average_rating()
    
    def get_discount_price(self, obj):
        return obj.discount_price

class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = '__all__'