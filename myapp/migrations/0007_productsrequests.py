# Generated by Django 5.0 on 2023-12-16 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_item_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='productsrequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]