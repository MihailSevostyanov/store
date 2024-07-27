from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    """Получает данные по продуктам из кеша, если кеш пуст, получает данные из БД"""
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "product_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products

def get_category_from_cache(recached: bool = False):
    if CACHE_ENABLED:
        key = f'category_list'
        if recached:
            category_list = Category.objects.all()
            cache.set(key, category_list)
        else:
            category_list = cache.get(key)
            if category_list is None:
                category_list = Category.objects.all()
                cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list