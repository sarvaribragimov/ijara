# Generated by Django 4.2 on 2023-04-07 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_kvartera_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kvartera',
            name='year_of_construction',
        ),
    ]
