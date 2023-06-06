# Generated by Django 4.2.2 on 2023-06-06 20:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядок')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.menu', verbose_name='Родительский раздел')),
            ],
            options={
                'verbose_name': 'Раздел меню',
                'verbose_name_plural': 'Разделы меню',
                'ordering': ('parent', 'order'),
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Содержание')),
                ('file', models.FileField(blank=True, null=True, upload_to='docs', verbose_name='Файл')),
                ('video_link', models.URLField(verbose_name='Ссылка на видео')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.menu', verbose_name='Раздел меню')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('menu', 'title'),
            },
        ),
    ]
