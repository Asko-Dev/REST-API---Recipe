# Generated by Django 2.1.15 on 2020-03-26 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingreditent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingreditent',
            new_name='Ingredient',
        ),
    ]
