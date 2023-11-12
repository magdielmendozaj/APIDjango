# Generated by Django 3.2.4 on 2023-11-12 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20231111_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sexo'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='especialidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.especialidad'),
        ),
    ]
