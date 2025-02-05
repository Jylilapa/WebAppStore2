from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to="fhoto/blog_images", null=True, blank=True, verbose_name="Изображение")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    publication = models.BooleanField(default=True, verbose_name="Признак публикации")
    counter_views = models.PositiveIntegerField(verbose_name="Количество просмотров", default=0)

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["title"]

    def __str__(self):
        return self.title
