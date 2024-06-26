# Generated by Django 4.1.7 on 2023-03-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0023_remove_episode_release'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorymovie',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='categorymovie',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='detailmovie',
            name='description',
        ),
        migrations.AddField(
            model_name='detailmovie',
            name='imdb_rating',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detailmovie',
            name='release',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detailmovie',
            name='rotten_rating',
            field=models.TextField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detailmovie',
            name='synopsis',
            field=models.TextField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detailmovie',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
