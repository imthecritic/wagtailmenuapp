# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 13:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20160620_1355'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_item_ptr',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
    ]
