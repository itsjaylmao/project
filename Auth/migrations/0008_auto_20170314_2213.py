# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 14:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0007_auto_20170314_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='Wxwpoezr9LPwnvZIszJDcoJ8', max_length=24),
        ),
    ]
