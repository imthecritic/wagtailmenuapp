# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 18:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_auto_20160621_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu_item',
            name='childpage',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childpage', to='wagtailcore.Page'),
        ),
    ]
