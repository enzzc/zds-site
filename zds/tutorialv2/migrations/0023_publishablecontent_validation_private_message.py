# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-26 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0004_python_3'),
        ('tutorialv2', '0027_auto_20190912_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='publishablecontent',
            name='validation_private_message',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='mp.PrivateTopic', verbose_name='Message de suivi staff'),
        ),
    ]