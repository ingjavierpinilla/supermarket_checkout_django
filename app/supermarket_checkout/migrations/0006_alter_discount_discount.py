# Generated by Django 4.0.2 on 2022-02-15 14:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_checkout', '0005_alter_discount_min_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)]),
        ),
    ]
