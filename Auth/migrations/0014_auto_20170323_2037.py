# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0013_auto_20170318_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='Z1UTSPz2CFEiVm4VQqVyJDlb', max_length=24),
        ),
    ]
