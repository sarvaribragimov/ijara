# Generated by Django 4.2 on 2023-04-10 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_is_active'),
        ('post', '0016_kvartera_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kvartera',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]