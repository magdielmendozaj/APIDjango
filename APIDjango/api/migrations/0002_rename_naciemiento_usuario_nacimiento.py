# Generated by Django 3.2.4 on 2023-10-06 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='naciemiento',
            new_name='nacimiento',
        ),
    ]
