"""
Models:
    - Submit:  提交。
"""

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class Submit(models.Model):
    """提交"""

    class Meta:
        verbose_name = '提交'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    C = 'C'
    CPP = 'CPP'
    LANGUAGE_CHOICES = ((C, 'C'),
                        (CPP, 'C++'),)

    JUDGE_PENDING = 'P'
    JUDGE_JUDGING = 'J'
    JUDGE_COMPLETED = 'C'
    JUDGE_STATUS_CHOICES = ((JUDGE_PENDING, '等待中'),
                            (JUDGE_JUDGING, '判题中'),
                            (JUDGE_COMPLETED, '已完成判题'),)

    COMPILE_OK = 'O'
    COMPILE_ERROR = 'E'
    COMPILE_STATUS_CHOICES = ((COMPILE_OK, '编译成功'),
                              (COMPILE_ERROR, '编译失败'),)

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

    judge_status = models.CharField(
        verbose_name='判题状态',
        max_length=1,
        choices=JUDGE_STATUS_CHOICES,
        default=JUDGE_PENDING,
        db_index=True,)
    compile_status = models.CharField(
        verbose_name='编译状态',
        max_length=1,
        choices=COMPILE_STATUS_CHOICES,
        blank=True,)
    run_results = JSONField(
        verbose_name='运行结果',
        help_text='[[status, time, memory]...], time in ms, memory in KB.',
        blank=True, null=True,)
    error_message = models.TextField(
        verbose_name='错误消息',
        blank=True,)
    score = models.FloatField(
        verbose_name='得分',
        help_text='得分使用 100 分制',
        blank=True, null=True,
        db_index=True,)

    create_time = models.DateTimeField(
        verbose_name='提交时间',
        default=timezone.now,)

    def __str__(self):
        return str(self.pk)

    def get_codefile_suffix(self):
        if self.language == Submit.C:
            return '.c'
        elif self.language == Submit.CPP:
            return '.cpp'
