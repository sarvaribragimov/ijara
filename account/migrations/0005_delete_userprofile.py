# Generated by Django 4.2 on 2023-04-10 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
