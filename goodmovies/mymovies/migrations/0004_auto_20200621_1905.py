# Generated by Django 2.2.6 on 2020-06-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymovies', '0003_auto_20200621_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='movie',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
