# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20170820_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='accept_cnt',
            field=models.BigIntegerField(default=0, verbose_name='通过次数'),
        ),
        migrations.AddField(
            model_name='problem',
            name='submit_cnt',
            field=models.BigIntegerField(default=0, help_text='只记录成功完成判题的提交', verbose_name='提交次数'),
        ),
    ]
