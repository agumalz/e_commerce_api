from rest_framework import serializers
from .models import CartModel
from product.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    product_weight = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()

    def get_product_weight(self, obj):
        return obj.quantity * obj.product.product_weight if obj.product else 0

    def get_price(self, obj):
        return obj.quantity * obj.product.price if obj.product else 0
    
    # def get_total_weight(self, obj):
    # def get_total_product_weight(self, obj):
    #     calculated_weight = self.get_product_weight(obj)
    #     if calculated_weight > 100:
    #         return "Over Weight"
    #     else:
    #         return calculated_weight
    
    class Meta:
        model = CartModel
        fields = ['product', 'quantity', 'product_weight', 'price']
