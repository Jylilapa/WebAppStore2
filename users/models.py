from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=30, verbose_name="Номер телефона", null=True, blank=True)
    avatar = models.ImageField(upload_to="users/avatars/", verbose_name="Аватар",null=True, blank=True)
    country = models.CharField(max_length=30, verbose_name="Страна", null=True, blank=True)
    token = models.CharField(max_length=100, verbose_name="Token", null=True, blank=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
