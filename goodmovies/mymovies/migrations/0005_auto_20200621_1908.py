# Generated by Django 2.2.6 on 2020-06-21 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovies', '0004_auto_20200621_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='movie',
            field=models.SlugField(max_length=255, unique=True, verbose_name='movie'),
        ),
    ]
