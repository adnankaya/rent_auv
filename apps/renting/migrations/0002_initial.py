# Generated by Django 5.0.3 on 2024-03-07 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('renting', '0001_initial'),
        ('uav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='renting',
            name='uav',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uav.uav'),
        ),
    ]