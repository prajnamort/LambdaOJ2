from django.db import models
from django.contrib.auth.models import AbstractUser


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
        },)
    student_id = models.CharField(
        verbose_name='学号',
        max_length=20,
        blank=True,)
