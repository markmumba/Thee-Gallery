# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-26 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0004_auto_20190825_2147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='post_date',
        ),
    ]
