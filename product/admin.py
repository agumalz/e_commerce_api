from django.contrib import admin
from product.models import ProductModel 

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'stock_quantity','product_weight','price','category', 'created_at', 'updated_at')
    
admin.site.register(ProductModel, ProductAdmin)    