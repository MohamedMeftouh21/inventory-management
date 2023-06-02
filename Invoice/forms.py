from django import forms
from dal import autocomplete
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        widget=autocomplete.ModelSelect2(url='product-autocomplete')
    )

    class Meta:
        model = Product
        fields = ['name']
