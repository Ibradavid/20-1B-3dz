from django.db import models

# Create your models here.
class Library(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок книги',
        null=False, blank=False
        )
    author = models.CharField(
        max_length=255,
        verbose_name='Автор книги',
        null=False, blank=False
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание',
        )
    paseg = models.CharField(
        max_length=100,
        verbose_name='Количество страниц',
        null=False, blank=False
    )
    image = models.ImageField(
        upload_to='library',
        verbose_name='Фото',
        null=True, blank=True
    )
    
    
    def __str__(self):
        return self.title