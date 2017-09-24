from django.db import models, transaction
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractUser

from main.utils.string_utils import generate_noise
from main.utils.user_utils import validate_multiuser_csv


class User(AbstractUser):
    """用户"""

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    email = models.EmailField(
        verbose_name='邮箱',
        unique=True,
        error_messages={
            'unique': '拥有该邮箱的用户已存在。',
        },
        blank=True, null=True,)
    mobile = models.CharField(
        verbose_name='手机号',
        max_length=11,
        blank=True, null=True,
        validators=[validators.RegexValidator(
            r'^\d{11}$', '请输入合法的手机号。', 'invalid'
        )],
        help_text='11 位数字',)
    student_id = models.CharField(
        verbose_name='学号',
        max_length=20,
        blank=True, null=True,)

    def save(self, *args, **kwargs):
        if self.email == '':
            self.email = None
        if self.mobile == '':
            self.mobile = None
        if self.student_id == '':
            self.student_id = None
        super().save(*args, **kwargs)


class MultiUserUpload(models.Model):
    """批量用户上传"""

    class Meta:
        verbose_name = '批量用户上传'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    csv_content = models.TextField(
        verbose_name='用户信息',
        validators=[validate_multiuser_csv],
        help_text='CSV 格式："username,student_id,email,mobile"，其中 username 字段为必填项')
    results = models.TextField(
        verbose_name='创建结果',
        help_text='CSV 格式："username,password"')
    create_time = models.DateTimeField(
        verbose_name='创建时间',
        default=timezone.now,)

    def __str__(self):
        return '%s' % self.id

    def save(self, *args, **kwargs):
        with transaction.atomic():
            lines = self.csv_content.splitlines()
            lines = [line.strip() for line in lines if line.strip()]
            results = []
            for line in lines:
                fields = [field.strip() for field in line.split(',')]
                assert len(fields) == 4
                username, student_id, email, mobile = fields
                assert username
                user = User.objects.create(
                    username=username,
                    student_id=student_id,
                    email=email,
                    mobile=mobile,)
                # password = generate_noise(8)
                password = username
                user.set_password(password)
                user.save()
                results.append('{},{}'.format(username, password))
            self.results = '\n'.join(results)
            super().save(*args, **kwargs)
