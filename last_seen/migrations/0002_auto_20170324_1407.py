# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 06:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('last_seen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lastseen',
            options={'ordering': ('-last_seen',), 'verbose_name': 'last seen'},
        ),
    ]
