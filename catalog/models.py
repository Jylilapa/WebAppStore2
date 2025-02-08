from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", null=True, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="catalog/images", null=True, blank=True, verbose_name="Изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(auto_now=True, verbose_name="Дата последнего изменения")
    publish_product = models.BooleanField(default=False, verbose_name="Опубликовано")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Владелец")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]
        permissions = [("can_unpublish_product", "Can unpublish product")]

    def __str__(self):
        return self.name
