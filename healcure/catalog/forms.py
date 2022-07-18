from django import forms
from datetime import date

from django.forms import ModelForm
from .models import Product



class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'main_desc', 'price']
