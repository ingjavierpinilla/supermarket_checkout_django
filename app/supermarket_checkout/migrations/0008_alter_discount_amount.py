# Generated by Django 4.0.2 on 2022-02-15 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_checkout', '0007_rename_min_amount_discount_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='amount',
            field=models.BigIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
