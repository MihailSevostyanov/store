from django import forms
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView

from catalog.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "preview", "category", "price"]

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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductListView(ListView):
    model = Product

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data["version"] = "Список продуктов"


class ProductDetailView(DetailView):
    model = Product


class ContactsView(TemplateView):
    template_name = "contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Контакты"
        return context
