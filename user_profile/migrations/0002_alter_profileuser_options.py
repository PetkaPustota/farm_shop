# Generated by Django 4.2.7 on 2023-11-27 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profileuser',
            options={'ordering': ('first_name',), 'verbose_name': 'Профиль', 'verbose_name_plural': 'Профили'},
        ),
    ]
