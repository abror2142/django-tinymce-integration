from django import forms

from tinymce.widgets import TinyMCE
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            "name": forms.widgets.TextInput(attrs={"class": "product-name", "id": "productNameId"}),
            "price": forms.widgets.NumberInput(attrs={"class": "product-price", "id": "productPriceId"})
        }