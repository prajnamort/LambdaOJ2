"""
Models:
    - Submit:  提交。
"""

from django.db import models
from django.utils import timezone


class Submit(models.Model):
    """提交"""

    class Meta:
        verbose_name = '提交'
        verbose_name_plural = verbose_name

    C = 'C'
    CPP = 'CPP'
    LANGUAGE_CHOICES = ((C, 'C'),
                        (CPP, 'C++'),)

    user = models.ForeignKey(
        to='User',
        verbose_name='提交者',
        related_name='submit_set',)
    problem = models.ForeignKey(
        to='Problem',
        verbose_name='题目',
        related_name='submit_set',)
    language = models.CharField(
        verbose_name='语言',
        max_length=5,
        choices=LANGUAGE_CHOICES,)
    code = models.TextField(
        verbose_name='代码',)

    create_time = models.DateTimeField(
        verbose_name='提交时间',
        default=timezone.now,)

    def __str__(self):
        return str(self.pk)
