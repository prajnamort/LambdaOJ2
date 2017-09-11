"""
Models:
    - Problem:  题目。
    - TestData:  测试数据。
"""

from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField

from main.utils.compare_utils import (validate_compare_file,
                                      get_compare_func,
                                      default_compare_func)


class Problem(models.Model):
    """题目"""

    class Meta:
        verbose_name = '题目'
        verbose_name_plural = verbose_name
        ordering = ['number']

    number = models.PositiveIntegerField(
        verbose_name='题目编号',
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
    desc = RichTextUploadingField(
        verbose_name='题目描述',)
    input_desc = RichTextUploadingField(
        verbose_name='输入描述',
        blank=True,)
    output_desc = RichTextUploadingField(
        verbose_name='输出描述',
        blank=True,)
    input_sample = models.TextField(
        verbose_name='输入样例',
        blank=True,)
    output_sample = models.TextField(
        verbose_name='输出样例',
        blank=True,)
    hint = RichTextUploadingField(
        verbose_name='提示',
        blank=True,)
    deadline = models.DateTimeField(
        verbose_name='截止日期',
        help_text='过期的提交，计算成绩时会打折扣。',)
    released = models.BooleanField(
        verbose_name='是否已发布',
        default=False,
        help_text='普通学生账号只能看到已发布的题目。',
        db_index=True,)
    contributor = models.CharField(
        verbose_name='题目贡献者',
        max_length=40,
        blank=True,)
    compare_file = models.FileField(
        verbose_name='Compare 函数文件',
        upload_to='uploads/judge/',
        validators=[validate_compare_file],
        help_text='请实现 compare_func 以自定义比较函数，例：def compare_func(answer, output): return True',
        blank=True,)

    submit_cnt = models.BigIntegerField(
        verbose_name='提交次数',
        help_text='只记录成功完成判题的提交',
        default=0,)
    accept_cnt = models.BigIntegerField(
        verbose_name='通过次数',
        default=0,)

    create_time = models.DateTimeField(
        verbose_name='创建时间',
        default=timezone.now,)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.contributor = self.contributor.strip()
        if self.contributor == '':
            self.contributor = 'Miku Chan'
        super().save(*args, **kwargs)

    @property
    def compare_func(self):
        if self.compare_file:
            return get_compare_func(self.compare_file.path)
        else:
            return default_compare_func

    @property
    def testdata_num(self):
        """测试数据总数"""
        return self.testdata_set.count()

    @property
    def accept_rate(self):
        if self.submit_cnt == 0:
            return '%.2f%%' % 0.0
        else:
            return '%.2f%%' % (100.0 * (self.accept_cnt / self.submit_cnt))


class TestData(models.Model):
    """测试数据"""

    class Meta:
        verbose_name = '测试数据'
        verbose_name_plural = verbose_name
        ordering = ['order']

    order = models.PositiveIntegerField(
        verbose_name='顺序',
        db_index=True,)
    problem = models.ForeignKey(
        to='Problem',
        verbose_name='题目',
        related_name='testdata_set',)
    input_file = models.FileField(
        verbose_name='输入文件',
        upload_to='uploads/',)
    output_file = models.FileField(
        verbose_name='输出文件',
        upload_to='uploads/',)

    create_time = models.DateTimeField(
        verbose_name='创建时间',
        default=timezone.now,)

    def __str__(self):
        return '%s' % self.order
