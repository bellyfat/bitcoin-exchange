# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-21 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0008_auto_20170820_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='wallets',
            name='amount',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=19),
        ),
    ]
