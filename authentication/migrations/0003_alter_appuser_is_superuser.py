# Generated by Django 4.2.7 on 2023-12-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_appuser_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
