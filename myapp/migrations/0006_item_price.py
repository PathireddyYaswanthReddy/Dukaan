# Generated by Django 5.0 on 2023-12-16 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_checkout_user_alter_orders_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
