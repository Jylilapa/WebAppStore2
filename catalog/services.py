from django.core.cache import cache

from catalog.models import Product, Category
from config.settings import CACHE_ENABLED


def get_product_from_cache():
    if not CACHE_ENABLED:
        return Product.objects.all()
    key = "products_list"
    products = cache.get(key)
    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


class ProductsListCategory:

    @staticmethod
    def get_products_category(category):
        products = Product.objects.filter(category=category)
        return products
