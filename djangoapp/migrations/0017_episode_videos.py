# Generated by Django 4.1.7 on 2023-03-22 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0016_episode_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='videos',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
    ]
