# Generated by Django 5.0 on 2023-12-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReBuy', '0003_categories_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='draft',
        ),
        migrations.AddField(
            model_name='product',
            name='daily_deal',
            field=models.BooleanField(default=False, verbose_name='Daily Deal'),
        ),
    ]