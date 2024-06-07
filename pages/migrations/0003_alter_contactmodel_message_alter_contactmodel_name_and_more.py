# Generated by Django 4.2.13 on 2024-06-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_usercommentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='message',
            field=models.TextField(verbose_name='message'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='subject'),
        ),
        migrations.AlterField(
            model_name='usercommentmodel',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='usercommentmodel',
            name='name',
            field=models.CharField(max_length=128, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='usercommentmodel',
            name='profession',
            field=models.CharField(max_length=128, verbose_name='profession'),
        ),
    ]