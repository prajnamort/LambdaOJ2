# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-20 15:55
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170820_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='run_results',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, help_text='[[status, time, memory]...], time in ms, memory in KB.', null=True, verbose_name='运行结果'),
        ),
    ]
