from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название статьи')
    text = models.TextField(blank=True, verbose_name='Текст статьи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Метка публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = ['-created_at', 'title']


class Category(models.Model):
    title = models.CharField(max_length=50, db_index=True, verbose_name='Название категории')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['-id']
