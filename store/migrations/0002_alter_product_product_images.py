# Generated by Django 4.2.6 on 2023-10-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_images',
            field=models.ImageField(upload_to='products'),
        ),
    ]
