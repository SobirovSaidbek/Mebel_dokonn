# Generated by Django 4.2.13 on 2024-06-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productcommentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategorymodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='productcolormodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='productmanufacture',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='long_description',
            field=models.TextField(verbose_name='long_description'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='short_description',
            field=models.CharField(max_length=255, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='productsizemodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='producttagmodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
    ]