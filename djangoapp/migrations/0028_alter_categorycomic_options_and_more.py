# Generated by Django 4.1.7 on 2023-04-05 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0027_episode_name_season_name_series_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorycomic',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='categorycomic',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='detailshop',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marvelheroes',
            name='title',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='marvelvillain',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategorycomic',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detailcomic',
            name='comics',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='detailheroes',
            name='images',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='detailheroes',
            name='multiverse',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailheroes',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailheroes',
            name='story',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='detailshop',
            name='items',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.shop'),
        ),
        migrations.AlterField(
            model_name='detailshop',
            name='photos',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='detailshop',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailshop',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailvillain',
            name='images',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='detailvillain',
            name='multiverse',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailvillain',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='detailvillain',
            name='story',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='marvelheroes',
            name='images',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='marvelheroes',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='marvelvillain',
            name='images',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='marvelvillain',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shop',
            name='cover',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shop',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='subcategorycomic',
            name='covers',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='subcategorycomic',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
