# Generated by Django 4.2 on 2023-04-10 10:00

from django.db import migrations, models
import post.file_renamer


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0020_remove_kvartera_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvartera',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=post.file_renamer.PathAndRename('posts')),
        ),
    ]
