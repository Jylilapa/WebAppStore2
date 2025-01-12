from itertools import product
from venv import create

from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name="Электроника", description="Бытовая техника и электроника")

        products = [
            {"name": "Мультиварка", "description": "Умная мультиварка", "category": category, "price": 5000},
            {"name": "Пылесос", "description": "Очень удобный пылесос", "category": category, "price": 7000},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Добавление продукта {product.name} прошло успешно"))
            else:
                self.stdout.write(self.style.WARNING(f"Продукт {product.name} был добавлен ранее"))
