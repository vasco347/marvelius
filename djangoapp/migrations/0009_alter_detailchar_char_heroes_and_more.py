# Generated by Django 4.1.7 on 2023-03-13 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0008_marvelheroes_marvelvillain_detailchar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailchar',
            name='char_heroes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.marvelheroes'),
        ),
        migrations.AlterField(
            model_name='detailchar',
            name='char_villain',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.marvelvillain'),
        ),
    ]