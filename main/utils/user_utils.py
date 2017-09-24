from django.core.exceptions import ValidationError


def validate_multiuser_csv(value):
    def _validate():
        from main.models import User

        lines = value.splitlines()
        lines = [line.strip() for line in lines if line.strip()]
        for line in lines:
            fields = [field.strip() for field in line.split(',')]
            if len(fields) != 4:
                raise ValidationError('格式错误，字段必须为 4 个，非必填可留空')
            username, student_id, email, mobile = fields
            if not username:
                raise ValidationError('用户名不可为空')
            if User.objects.filter(username=username).exists():
                raise ValidationError('用户名 {} 已存在'.format(username))
            if User.objects.filter(email=email).exists():
                raise ValidationError('邮箱 {} 已存在'.format(email))

    try:
        _validate()
    except ValidationError as e:
        raise e
    except Exception as e:
        message = str(e) or 'CSV 格式或内容错误，请检查。'
        raise ValidationError(message)
