# Generated by Django 4.1.7 on 2023-03-26 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0024_alter_categorymovie_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailmovie',
            name='imdb_rating',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailmovie',
            name='release',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailmovie',
            name='rotten_rating',
            field=models.CharField(max_length=100),
        ),
    ]