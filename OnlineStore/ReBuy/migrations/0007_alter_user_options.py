# Generated by Django 5.0 on 2023-12-23 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReBuy', '0006_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
