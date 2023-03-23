# Generated by Django 4.1.7 on 2023-03-22 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0018_series_cast_series_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='series',
            name='total_episode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='series',
            name='cast',
            field=models.CharField(max_length=2000),
        ),
    ]