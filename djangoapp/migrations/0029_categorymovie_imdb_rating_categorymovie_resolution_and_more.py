# Generated by Django 4.1.7 on 2023-04-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0028_alter_categorycomic_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymovie',
            name='imdb_rating',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorymovie',
            name='resolution',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='categorymovie',
            name='rotten_rating',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
