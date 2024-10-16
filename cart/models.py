from django.db import models
from product.models import ProductModel

# Create your models here.
class CartModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    