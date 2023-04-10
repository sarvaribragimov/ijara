# Generated by Django 4.2 on 2023-04-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0022_kvartera_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kvartera',
            name='user',
        ),
        migrations.AddField(
            model_name='kvartera',
            name='vositachilik_haqi',
            field=models.CharField(choices=[('ha', 'ha'), ('yuq', 'yuq')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]
