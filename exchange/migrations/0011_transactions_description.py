# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-21 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0010_auto_20170821_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='description',
            field=models.CharField(default='null', max_length=250),
        ),
    ]
