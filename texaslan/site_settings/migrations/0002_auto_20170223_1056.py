# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-23 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sitesettings',
            options={'verbose_name_plural': 'Site Settings'},
        ),
    ]