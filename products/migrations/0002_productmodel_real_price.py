# Generated by Django 4.2.13 on 2024-06-05 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='real_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
