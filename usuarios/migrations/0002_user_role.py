# Generated by Django 3.2.6 on 2021-08-29 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('Ventas', 'Ventas'), ('Compras', 'Compras')], default='', max_length=40),
        ),
    ]
