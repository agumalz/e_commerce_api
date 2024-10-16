from django import forms
from product.models import ProductModel

class CartForm(forms.Form):
    product = forms.ModelChoiceField(queryset=ProductModel.objects.all())
    quantity = forms.IntegerField()

class LocationForm(forms.Form):
    origin = forms.CharField(max_length=255, widget=forms.TextInput)
    destination = forms.CharField(max_length=255, widget=forms.TextInput)