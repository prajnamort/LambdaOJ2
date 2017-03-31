"""
Models:
    - Problem:  问题。
"""

from django.db import models
from django.utils import timezone


class Problem(models.Model):
    """
    问题。
    """

    class Meta:
        verbose_name = '问题'
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

    create_time = models.DateTimeField(
        verbose_name='创建时间',
        default=timezone.now,)
