# Generated by Django 5.0 on 2023-12-23 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReBuy', '0005_mainpageslider_product_price_alter_product_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, verbose_name='Username')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
            ],
        ),
    ]
