# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-24 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import main.utils.user_utils


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20170924_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='multiuserupload',
            name='csv_content',
            field=models.TextField(help_text='CSV 格式："username,student_id,email,mobile"，其中 username 字段为必填项', validators=[main.utils.user_utils.validate_multiuser_csv], verbose_name='用户信息'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='学号'),
        ),
    ]
