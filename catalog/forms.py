from django import forms
from django.forms import ModelForm, BooleanField

from catalog.models import Product, Version


class StyleFormMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "preview", "category", "price",)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for product in prohibited_words:
            if product in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово: {product}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        for product in prohibited_words:
            if product in cleaned_data:
                raise forms.ValidationError(f'Нельзя использовать слово: {product}')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'in_stock',)


class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
