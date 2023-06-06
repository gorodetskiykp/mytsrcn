from django.db import models
from django.utils.timezone import now


class Menu(models.Model):
    title = models.CharField('Название', max_length=200)
    slug = models.SlugField(blank=True, null=True, unique=True)
    order = models.PositiveSmallIntegerField('Порядок')
    ext_link = models.URLField('Внешняя ссылка', null=True, blank=True)
    parent = models.ForeignKey('Menu', verbose_name='Родительский раздел', on_delete=models.SET_NULL, null=True,
                               blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = 'order',
        verbose_name = 'Раздел меню'
        verbose_name_plural = 'Разделы меню'


class Article(models.Model):
    title = models.CharField('Название', max_length=200)
    body = models.TextField('Содержание', null=True, blank=True)
    file = models.FileField('Файл', upload_to='media/docs', null=True, blank=True)
    video_link = models.URLField('Ссылка на видео', null=True, blank=True)
    created = models.DateTimeField('Дата', default=now)
    menu = models.ForeignKey('Menu', verbose_name='Раздел меню', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = 'menu', 'title'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class News(models.Model):
    title = models.CharField('Название', max_length=200)
    body = models.TextField('Содержание', null=True, blank=True)
    file = models.ImageField('Файл', upload_to='media/news', null=True, blank=True)
    created = models.DateTimeField('Дата', default=now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = 'title',
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'