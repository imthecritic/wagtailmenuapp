# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 18:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0028_merge'),
        ('menu', '0013_auto_20160622_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='page_5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='page_title5',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]