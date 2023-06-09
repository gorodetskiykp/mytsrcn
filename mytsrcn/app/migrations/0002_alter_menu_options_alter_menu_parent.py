# Generated by Django 4.2.2 on 2023-06-06 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ('order',), 'verbose_name': 'Раздел меню', 'verbose_name_plural': 'Разделы меню'},
        ),
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.menu', verbose_name='Родительский раздел'),
        ),
    ]
