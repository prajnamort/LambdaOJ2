# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-17 07:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20170911_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiUserUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('csv_content', models.TextField(help_text='CSV 格式："username,student_id,email,mobile"，其中 username 字段为必填项', verbose_name='用户信息')),
                ('results', models.TextField(help_text='CSV 格式："username,password"', verbose_name='创建结果')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '批量用户上传',
                'verbose_name_plural': '批量用户上传',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, help_text='11 位数字', max_length=11, null=True, validators=[django.core.validators.RegexValidator('^\\d{11}$', '请输入合法的手机号。', 'invalid')], verbose_name='手机号'),
        ),
    ]