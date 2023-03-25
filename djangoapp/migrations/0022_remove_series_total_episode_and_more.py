# Generated by Django 4.1.7 on 2023-03-24 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0021_episode_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='series',
            name='total_episode',
        ),
        migrations.RemoveField(
            model_name='series',
            name='total_season',
        ),
        migrations.AddField(
            model_name='episode',
            name='release',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='imdb_rating',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='release',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='series',
            name='rotten_rating',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='episode',
            name='title',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(max_length=2000),
        ),
    ]