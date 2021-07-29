# Generated by Django 3.2.5 on 2021-07-12 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210708_2133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='news.category', verbose_name='Категория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
    ]
