"""
Models:
    - Submit:  提交。
"""

import os

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.postgres.fields import JSONField


class Submit(models.Model):
    """提交"""

    class Meta:
        verbose_name = '提交'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    C89 = 'C89'
    C99 = 'C99'
    C11 = 'C11'
    CPP03 = 'C++03'
    CPP11 = 'C++11'
    LANGUAGE_CHOICES = ((C89, 'C89'),
                        (C99, 'C99'),
                        (C11, 'C11'),
                        (CPP03, 'C++03'),
                        (CPP11, 'C++11'),)

    JUDGE_PENDING = 'P'
    JUDGE_JUDGING = 'J'
    JUDGE_COMPLETED = 'C'
    JUDGE_FAILED = 'F'
    JUDGE_STATUS_CHOICES = ((JUDGE_PENDING, '等待中'),
                            (JUDGE_JUDGING, '判题中'),
                            (JUDGE_COMPLETED, '已完成判题'),
                            (JUDGE_FAILED, '判题失败'),)

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
        if self.language in [Submit.C89, Submit.C99, Submit.C11]:
            return '.c'
        elif self.language in [Submit.CPP03, Submit.CPP11]:
            return '.cpp'

    @property
    def codefile_name(self):
        return 'source%s' % self.get_codefile_suffix()

    def copy_code_to_dir(self, code_dir):
        code_path = os.path.join(code_dir, self.codefile_name)
        with open(code_path, 'w') as f:
            f.write(self.code)

    def get_compiler_name(self):
        return self.language.lower()
