# Generated by Django 4.1.5 on 2023-04-11 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='idcliente',
        ),
        migrations.RemoveField(
            model_name='compras',
            name='idproducto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='idproducto',
        ),
    ]
