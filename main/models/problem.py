"""
Models:
    - Problem:  题目。
"""

from django.db import models
from django.utils import timezone


class Problem(models.Model):
    """题目"""

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name
        ordering = ['order']

    order = models.PositiveIntegerField(
        verbose_name='顺序',
        unique=True,)
    title = models.CharField(
        verbose_name='标题',
        max_length=100,)
    time_limit = models.IntegerField(
        verbose_name='时间限制',
        help_text='单位为 s',)
    memory_limit = models.IntegerField(
        verbose_name='内存限制',
        help_text='单位为 KB',)
    desc = models.TextField(
        verbose_name='题目描述',)
    input_desc = models.TextField(
        verbose_name='输入描述',
        blank=True,)
    output_desc = models.TextField(
        verbose_name='输出描述',
        blank=True,)
    input_sample = models.TextField(
        verbose_name='输入样例',
        blank=True,)
    output_sample = models.TextField(
        verbose_name='输出样例',
        blank=True,)
    hint = models.TextField(
        verbose_name='提示',
        blank=True,)
    sample_num = models.PositiveIntegerField(
        verbose_name='测试数据总数',)
    deadline = models.DateTimeField(
        verbose_name='截止日期',
        help_text='过期的提交，计算成绩时会打折扣。',)
    released = models.BooleanField(
        verbose_name='是否已发布',
        default=False,
        help_text='普通学生账号只能看到已发布的题目。',)
    contributor = models.TextField(
        verbose_name='题目贡献者',
        blank=True,)

    create_time = models.DateTimeField(
        verbose_name='创建时间',
        default=timezone.now,)
