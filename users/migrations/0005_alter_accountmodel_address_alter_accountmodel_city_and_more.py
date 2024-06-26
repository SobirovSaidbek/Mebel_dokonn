# Generated by Django 4.2.13 on 2024-06-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_accountmodel_address_alter_accountmodel_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountmodel',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='address'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='company'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='accountmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='phone'),
        ),
    ]
