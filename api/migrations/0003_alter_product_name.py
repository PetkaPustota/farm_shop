# Generated by Django 4.2.7 on 2023-12-05 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_product_brand_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(),
        ),
    ]
