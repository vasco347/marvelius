# Generated by Django 4.1.7 on 2023-03-12 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_categoryseries_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategorymovie',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
