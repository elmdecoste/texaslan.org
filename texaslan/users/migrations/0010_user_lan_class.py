# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-22 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170221_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lan_class',
            field=models.CharField(blank=True, choices=[('F', 'Founder'), ('A', 'Alpha'), ('B', 'Beta'), ('G', 'Gamma'), ('D', 'Delta'), ('E', 'Epsilon'), ('Z', 'Zera')], max_length=3, null=True),
        ),
    ]