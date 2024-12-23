# Generated by Django 5.1.2 on 2024-12-12 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_situacao_rename_description_car_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='situacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cars_situacao', to='cars.situacao'),
        ),
    ]