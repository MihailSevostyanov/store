from django.contrib import admin

from catalog.models import Category, Product, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'owner')
    list_filter = ('category', 'owner')
    search_fields = ('name', 'description')

@admin.register(Version)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'number_version', 'name', 'current_version')
    list_filter = ('current_version',)
    search_fields = ('name', 'number_version')
