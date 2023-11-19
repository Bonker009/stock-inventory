from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'unit_price', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'style': 'color: red;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        unit_price = cleaned_data.get('unit_price')
        quantity = cleaned_data.get('quantity')

        if unit_price and unit_price <= 0:
            self.add_error('unit_price', 'Unit price must be greater than zero.')

        if quantity and quantity <= 0:
            self.add_error('quantity', 'Quantity must be greater than zero.')

        return cleaned_data
